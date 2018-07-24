using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Dojo_League.Models;

using NinjaFactory.Factories;

namespace Dojo_League.Controllers
{

    public class HomeController : Controller
    {
        public ViewModel DashModel
        {
            get
            {
                IEnumerable<Ninja> ninjas = DbConnector.SelectNinjas();
                IEnumerable<Dojo> dojos = DbConnector.SelectDojos();
                ViewModel stuff = new ViewModel()
                {
                    Ninjas = ninjas,
                    Dojos = dojos
                };
                return stuff;
            }
        }

        
        [HttpGet("ninjas")]
        public IActionResult Ninjas()
        {   
            return View(DashModel);
        }            
        [HttpGet("ninja/{id}")]
        public IActionResult Ninja(int id)
        {
            ViewModel model = new ViewModel()
            {
                newninja = DbConnector.SelectNinjas(id),
                newdojo = DbConnector.SelectDojos(DbConnector.SelectNinjas(id).dojo)
            };
            return View(model);
        }            
        [HttpGet("dojos")]
        public IActionResult Dojos()
        {
            
            return View(DashModel);
        }            
         [HttpGet("dojo/{id}")]
        public IActionResult Dojo(int id)
        {
            Dojo dojo =DbConnector.SelectDojos(id);
            ViewModel model = new ViewModel()
            {
                newdojo = dojo,
                Ninjas = DbConnector.NinjasFromDojo(id),
                RogueNinjas = DbConnector.NinjasFromDojo(0)
            };
            
            return View(model);
        }            

        [HttpPost("Createninja")]
        public IActionResult CreateNinja(ViewModel model)
        {
            Ninja ninja = model.newninja;
            if (ModelState.IsValid)
            {
                
                DbConnector.AddNewNinja(ninja);
                return RedirectToAction("Ninjas");
            }
            else
            {
                ViewModel NinjaModel = DashModel;
                NinjaModel.newninja = ninja;
                return View("Ninjas",DashModel);
            }
        }
        [HttpPost("Createdojo")]
        public IActionResult CreateDojo(ViewModel model)
        {
            Dojo dojo = model.newdojo;
            if (ModelState.IsValid)
            {
                
                DbConnector.AddNewDojo(dojo);
                return RedirectToAction("Dojos");
            }
            else
            {
                ViewModel DojoModel = DashModel;
                DojoModel.newdojo = dojo;
                return View("Dojos",DashModel);
            }
        }
        [HttpPost("add")]
        public IActionResult add(int dojo_id, int ninja_id)
        {
            DbConnector.JoinDojo(dojo_id,ninja_id);
            Dojo dojo =DbConnector.SelectDojos(dojo_id);
            ViewModel model = new ViewModel()
            {
                newdojo = dojo,
                Ninjas = DbConnector.NinjasFromDojo(dojo_id),
                RogueNinjas = DbConnector.NinjasFromDojo(0)
            };
            

            return View("Dojo",model);
        }
        [HttpPost("Banish")]
        public IActionResult Banish(int dojo_id, int ninja_id)
        {
            DbConnector.Banish(ninja_id);
            Dojo dojo =DbConnector.SelectDojos(dojo_id);
            ViewModel model = new ViewModel()
            {
                newdojo = dojo,
                Ninjas = DbConnector.NinjasFromDojo(dojo_id),
                RogueNinjas = DbConnector.NinjasFromDojo(0)
            };
            
            return View("Dojo",model);
        }
    }
}
