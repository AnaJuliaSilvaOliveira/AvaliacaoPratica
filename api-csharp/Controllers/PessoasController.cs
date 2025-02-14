using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using CsvHelper;
using CsvImportApi.Data;
using CsvImportApi.Models;
using System.Globalization;
using System.Text.Json;

namespace CsvImportApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PessoasController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public PessoasController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpPost("importar-csv")]
        public async Task<IActionResult> ImportarCsv([FromForm] IFormFile file)
        {
            if (file == null || file.Length == 0)
                return BadRequest("Arquivo inválido.");

            using var reader = new StreamReader(file.OpenReadStream());
            using var csv = new CsvReader(reader, CultureInfo.InvariantCulture);
            var registros = csv.GetRecords<Pessoa>().ToList();

            await _context.Pessoas.AddRangeAsync(registros);
            await _context.SaveChangesAsync();

            return Ok("Dados importados com sucesso.");
        }
        
        // GET: api/pessoas/{id}
        [HttpGet("{id}")]
        public async Task<IActionResult> GetPessoa(int id)
        {
            var pessoa = await _context.Pessoas.FindAsync(id);
            if (pessoa == null)
                return NotFound(new { message = "Pessoa não encontrada." });

            return Ok(pessoa);
        }

        [HttpGet("exportar")]
        public async Task<IActionResult> ExportarParaJson()
        {
            var pessoas = await _context.Pessoas.ToListAsync();
             // Converte a lista de pessoas para JSON
            var json = JsonSerializer.Serialize(pessoas);
             // Salva o arquivo JSON no diretório raiz do projeto
            var filePath = Path.Combine(Directory.GetCurrentDirectory(), "query_response.json");
            await System.IO.File.WriteAllTextAsync(filePath, json);
             return Ok(new { message = "Arquivo JSON gerado com sucesso!", filePath });
        }
    }
}