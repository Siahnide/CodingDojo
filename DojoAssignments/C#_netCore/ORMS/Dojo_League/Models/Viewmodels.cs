using System.Collections.Generic;

namespace Dojo_League.Models
{
    public class ViewModel
    {
        public IEnumerable<Ninja> Ninjas {get;set;}
        public IEnumerable<Ninja> RogueNinjas {get;set;}
        public IEnumerable<Dojo> Dojos {get;set;}
        public Ninja newninja {get;set;}
        public Dojo newdojo {get;set;}
    }
}