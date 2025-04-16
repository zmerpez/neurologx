import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.*;
import org.apache.lucene.index.*;
import org.apache.lucene.store.*;

import java.io.*;
import java.nio.file.Paths;
import com.google.gson.*;

public class LuceneLogIndexer {

    public static void main(String[] args) throws Exception {
        // Go one level up to access data/logs.jsonl
        String logFilePath = "../data/logs.jsonl"; 
        String indexPath = "index";

        Directory dir = FSDirectory.open(Paths.get(indexPath));
        Analyzer analyzer = new StandardAnalyzer();
        IndexWriterConfig config = new IndexWriterConfig(analyzer);

        try (IndexWriter writer = new IndexWriter(dir, config)) {
            try (BufferedReader br = new BufferedReader(new FileReader(logFilePath))) {
                String line;
                Gson gson = new Gson();

                while ((line = br.readLine()) != null) {
                    JsonObject log = gson.fromJson(line, JsonObject.class);

                    Document doc = new Document();
                    doc.add(new StringField("timestamp", log.get("timestamp").getAsString(), Field.Store.YES));
                    doc.add(new StringField("level", log.get("level").getAsString(), Field.Store.YES));
                    doc.add(new StringField("component", log.get("component").getAsString(), Field.Store.YES));
                    doc.add(new TextField("message", log.get("message").getAsString(), Field.Store.YES));
                    doc.add(new StringField("label", log.get("label").getAsString(), Field.Store.YES));

                    writer.addDocument(doc);
                }
            }

            writer.commit();
            System.out.println("✅ Logs indexed to Lucene directory: " + indexPath);
        }
    }
}
