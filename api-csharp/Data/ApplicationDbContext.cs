using Microsoft.EntityFrameworkCore;
using CsvImportApi.Models;

namespace CsvImportApi.Data
{
    public class ApplicationDbContext : DbContext
    {
        public DbSet<Pessoa> Pessoas { get; set; }
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }
    }
}