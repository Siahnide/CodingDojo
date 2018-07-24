using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Lost.Models;
using DbConnection;

namespace Lost.Controllers
{
    public class HomeController : Controller
    {   
        [HttpGet("")]
        public IActionResult Index()
        {
            string query = "SELECT * FROM trails";
            
            ViewBag.trails = DbConnector.Query(query);
            return View();
        }

        [HttpGet("form")]
        public IActionResult Form()
        {
            return View();
        }

        [HttpPost("process")]
        public IActionResult Process(Trail trail)
        {

            if(ModelState.IsValid)
            {
                string query = $"INSERT INTO trails (name,description,length,elevation,longtitude,latitude) VALUES('{trail.name}','{trail.desc}','{trail.length}','{trail.elevation}','{trail.longtitude}','{trail.latitude}')";
                DbConnector.Query(query);
                return RedirectToAction("Index");
            }
            else{
                return View("Form");
            }
        }

        [HttpPost("single")]
        public IActionResult Trail(int id)
        {
            string query = $"SELECT * FROM trails WHERE(id='{id}')";
            ViewBag.trail = DbConnector.Query(query);
            return View();
        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
