using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using PartialsFunzies.Models;

namespace PartialsFunzies.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpGet("about")]

        public IActionResult About()
        {
            return RedirectToAction("Index");
        }
        [HttpGet("contact")]

        public IActionResult Contact()
        {
            return RedirectToAction("Index");
        }
        [HttpPost("survey")]
        public IActionResult Survey(Survey survey)
        {
            if(ModelState.IsValid)
            {

                return RedirectToAction("Index");
            }
            return View("Index");
        }
        [HttpGet("survey")]
        public IActionResult Survey()
        {
            return Json("SOMETHING ELSE");
        }
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
