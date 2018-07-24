using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Orpg.Models;

namespace Orpg.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost("Register")]
        public IActionResult Registration(User user)
        {
            if(ModelState.IsValid)
            {
                return View("Success");
            }
            else
            {
            return View("Index");

            }
        }
        public IActionResult Login(User user)
        {
            return View();
        }
    }
}
