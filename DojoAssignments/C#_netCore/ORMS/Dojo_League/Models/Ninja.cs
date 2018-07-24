using System.ComponentModel.DataAnnotations;
using NinjaFactory.Factories;
namespace Dojo_League.Models
{

    public class Ninja
    {
        
        public int id {get;set;}
        [Required]
        public string name {get;set;}
        [Required]
        [Range(1,10)]
        public int level {get;set;}
        [Required]
        public int dojo {get;set;}
        public void Join(int id)
        {
            dojo = id;
        }

        public Dojo _dojo()
        {
            return DbConnector.SelectDojos(dojo);
        }
        public string description {get;set;}
    }
}