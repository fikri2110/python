public class RunningTextFrame extends javax.swing.JFrame {
    
    private JLabel runningTextLabel;
    private Thread runningTextThread;

    /**
     * Creates new form RunningTextFrame
     */
    public RunningTextFrame() {
        initComponents();
        
        // Mengatur properties JLabel
        runningTextLabel.setText("Ini adalah contoh running text di Java NetBeans");
        runningTextLabel.setFont(new java.awt.Font("Tahoma", 0, 24)); // Sesuaikan dengan keinginan Anda
        runningTextLabel.setForeground(java.awt.Color.RED); // Sesuaikan dengan keinginan Anda
        
        // Membuat thread untuk mengatur running text
        runningTextThread = new Thread(() -> {
            while (true) {
                try {
                    // Menggeser teks dari kiri ke kanan
                    String labelText = runningTextLabel.getText();
                    String firstChar = labelText.substring(0, 1);
                    String remainingChars = labelText.substring(1);
                    runningTextLabel.setText(remainingChars + firstChar);
                    
                    // Memberi jeda selama 100 milidetik
                    Thread.sleep(100);
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
            }
        });
        
        // Memulai thread
        runningTextThread.start();
    }

    // Generated code from NetBeans
    // ...
}
