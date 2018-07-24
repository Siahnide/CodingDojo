using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using NinjaFactory.Factories;
namespace Dojo_League.Models
{
    public class Dojo
    {
        [Key]
        public int id {get;set;}
        public IEnumerable<Ninja> all_ninjas
        {
            get
            {
                return DbConnector.NinjasFromDojo(id);
            }
        
        }
        public string name{get;set;}
        public string location{get;set;}
        public string info{get;set;}
        public Dojo()
        {
            
                
            
        }
    }
}
