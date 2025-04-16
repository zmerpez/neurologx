import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.StoredFields;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.MatchAllDocsQuery;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Paths;

public class LuceneLogExporter {

    public static void main(String[] args) {
        String indexPath = "index";
        String outputFile = "../data/logs_export.csv";

        try (
            DirectoryReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(indexPath)));
            PrintWriter writer = new PrintWriter(new FileWriter(outputFile))
        ) {
            IndexSearcher searcher = new IndexSearcher(reader);
            MatchAllDocsQuery query = new MatchAllDocsQuery();
            TopDocs topDocs = searcher.search(query, reader.maxDoc());
            StoredFields storedFields = reader.storedFields();

            writer.println("timestamp,level,component,message,label");

            for (ScoreDoc sd : topDocs.scoreDocs) {
                Document doc = storedFields.document(sd.doc);

                String timestamp = escape(doc.get("timestamp"));
                String level     = escape(doc.get("level"));
                String component = escape(doc.get("component"));
                String message   = escape(doc.get("message"));
                String label     = escape(doc.get("label"));

                writer.printf("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"%n",
                        timestamp, level, component, message, label);
            }

            System.out.println("✅ Logs exported to: " + outputFile);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String escape(String input) {
        if (input == null) return "";
        return input.replace("\"", "\"\"");
    }
}
