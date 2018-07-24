using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using SessionFun.Models;

namespace SessionFun.Controllers
{
    public class HomeController : Controller
    {
	    [HttpGet("")]
        public IActionResult Index()
        {
            int? goldMaybe = HttpContext.Session.GetInt32("Gold");
            // Initialize Session 
            if(goldMaybe == null)
            {
                // set to zero!
                HttpContext.Session.SetInt32("Gold", 0);
                goldMaybe = 0;
            }
            ViewBag.Gold = goldMaybe;

            return View();
        }
        [HttpPost("gold")]
        public IActionResult Golding(string building)
        {
            if(building == "cavern")
            {

            }
            else if(building == "dragon")
            {

            }
            else if(building == "nana")
            {

            }
            else
            {

            }
            return RedirectToAction("Index");
        }
    }
}