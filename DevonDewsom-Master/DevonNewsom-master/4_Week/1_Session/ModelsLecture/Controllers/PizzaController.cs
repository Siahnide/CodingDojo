using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ModelsLecture.Models;

namespace ModelsLecture.Controllers
{
    public class PizzaController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost("create")]
        public IActionResult Create(Pizza pizza)
        {
            // ENTERING TO DB...
            TempData["Success"] = $"Thank you for submitting a PIZZA, {pizza.Name} sure sounds YUMMY!";
            return RedirectToAction("Pizzas");
        }
        [HttpGet("pizzas")]
        public IActionResult Pizzas()
        {
            Pizza[] model = new Pizza[]
            {
                new Pizza(){ Name="Big Dog Pizza",Topping="Hot Dogs"},
                new Pizza(){ Name="THE WOWZER",Topping="PEPS"},
                new Pizza(){ Name="MAS PICANTE",Topping="Habeneros"}
            };
            return View(model);
        }
        [HttpGet("pizza")]
        public IActionResult Show()
        {
            Pizza thePizza = new Pizza()
            {
                Name = "MAS PICANTE",
                Topping = "VENTE HABENEROS"
            };
            ViewBag.Pizza = thePizza;
            return View(thePizza);
        }
    }
}
