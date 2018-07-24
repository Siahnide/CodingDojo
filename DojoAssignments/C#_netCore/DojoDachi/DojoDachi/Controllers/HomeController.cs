using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using DojoDachi.Models;

namespace DojoDachi.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            HttpContext.Session.SetInt32("Meals",3);
            HttpContext.Session.SetInt32("Happiness",20);
            HttpContext.Session.SetInt32("Fullness",20);
            HttpContext.Session.SetInt32("Energy",50);
            ViewBag.Meals = HttpContext.Session.GetInt32("Meals");
            ViewBag.Happiness = HttpContext.Session.GetInt32("Happiness");
            ViewBag.Fullness = HttpContext.Session.GetInt32("Fullness");
            ViewBag.Energy = HttpContext.Session.GetInt32("Energy");
            return View();
        }


    }
}
