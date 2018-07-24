using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Random_Passcode.Models;
using Microsoft.AspNetCore.Http;

namespace Random_Passcode.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {

            return RedirectToAction("Randoms");
        }
        [HttpGet]
        [Route("Randoms")]
        public IActionResult Randoms()
        {
            HttpContext.Session.SetInt32("num",1);
            
            return View();
        }
        [HttpPost]
        [Route("Randoms_post")]
        public IActionResult Randoms_post()
        {
            int? v1 =HttpContext.Session.GetInt32("num");
            int v2 = v1.GetValueOrDefault();
            HttpContext.Session.SetInt32("num",v2 + 1);

            int? val =  HttpContext.Session.GetInt32("num");
            
            ViewBag.Num = val;
            
            return View("Randoms_post");
        }
    }
}
