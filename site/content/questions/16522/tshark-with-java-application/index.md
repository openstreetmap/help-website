+++
type = "question"
title = "tshark with Java Application"
description = '''Hi Everybody, This command is used with command line correctly: C:&#92;Program Files&#92;Wireshark&amp;gt;tshark -i 1 -w &quot;C:&#92;workspace&#92;runExternal&#92;myTestCap.pcap&quot;   -T text -V &amp;gt; &quot;C:&#92;workspace&#92;runExternal&#92;myTestCap.txt&quot; But I cannot run this with my Java Application. Can you help me how I can use this?'''
date = "2012-12-04T00:27:00Z"
lastmod = "2012-12-04T05:06:00Z"
weight = 16522
keywords = [ "torichelli" ]
aliases = [ "/questions/16522" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark with Java Application](/questions/16522/tshark-with-java-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16522-score" class="post-score" title="current number of votes">0</div><span id="post-16522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everybody,</p><p>This command is used with command line correctly: C:\Program Files\Wireshark&gt;tshark -i 1 -w "C:\workspace\runExternal\myTestCap.pcap" -T text -V &gt; "C:\workspace\runExternal\<a href="http://myTestCap.txt">myTestCap.txt</a>"</p><p>But I cannot run this with my Java Application.</p><p>Can you help me how I can use this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-torichelli" rel="tag" title="see questions tagged &#39;torichelli&#39;">torichelli</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 00:27</strong></p><img src="https://secure.gravatar.com/avatar/cd22dbf05dd19ca820e2b9c3e4216690?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kilicelli&#39;s gravatar image" /><p><span>kilicelli</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kilicelli has no accepted answers">0%</span></p></div></div><div id="comments-container-16522" class="comments-container"><span id="16537"></span><div id="comment-16537" class="comment"><div id="post-16537-score" class="comment-score"></div><div class="comment-text"><p>Here is the code; I want to listen my network and see the bytes like text format, and with continuousFileReader method I read the this("textCap.txt") text file...<br />
</p><p>public class ReadChangingFile {</p><pre><code>public static void main(String args[]) throws IOException, InterruptedException{

    String path = &quot;C:/workspace/runExternal&quot;;
    String execute = &quot;C:\\Progra~1\\Wireshark\\tshark -i 1 -w C:\\workspace\\runExternal\\testCap.pcap -T text -V &gt; C:\\workspace\\runExternal\\testCap.txt&quot;;

    try { 
        Runtime.getRuntime().exec(execute); 
    }catch (IOException e1) { 
        System.out.println(&quot;Error during initialization of live capture&quot;); 
        e1.printStackTrace(); 
    }

    Thread.sleep(5000);     
    continuousFileReader(path);
}

private static void continuousFileReader(String fileName) {
    String appFileName = fileName + &quot;/testCap.txt&quot;;

    File file = new File(appFileName);
    if(!(file.exists())){
        System.out.println(&quot;Relevant File Does Not Exist At &quot; +fileName+&quot; Hence Exiting System&quot;);
        System.exit(1);
    }

    long lengthBefore = 0;
    long length = 0;

    while(true){
        RandomAccessFile reader = null;
        try {
            if ((length = file.length()) &gt; lengthBefore) {
                try {
                    reader = new RandomAccessFile(file,&quot;r&quot;);
                    reader.seek(lengthBefore);
                    lengthBefore = length;
                    String line = null;
                    while (!((line = reader.readLine()) == null)) {
                        // do whatever with contents
                        //System.out.println(line);
                        if(line.contains(&quot;iMSI:&quot;)){
                            //System.out.println(line);

                            JOptionPane exJPane = new JOptionPane();
                            exJPane.showMessageDialog(null, line);

                            //JOptionPane.showConfirmDialog(null, line);

                        }
                    }
                } catch (FileNotFoundException ex) {
                    //handle exception
                }

                catch (IOException ex) {
                    //handle exception
                }

            }

            Thread.sleep(10000);
        } catch (InterruptedException ex) {
            try {
                if(reader!=null){
                    reader.close();
                }
            } catch (IOException ex1) {
                //handle exception
            }
        }
    }
}</code></pre><p>}</p></div><div id="comment-16537-info" class="comment-info"><span class="comment-age">(04 Dec '12, 05:06)</span> <span class="comment-user userinfo">kilicelli</span></div></div></div><div id="comment-tools-16522" class="comment-tools"></div><div class="clear"></div><div id="comment-16522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16531"></span>

<div id="answer-container-16531" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16531-score" class="post-score" title="current number of votes">0</div><span id="post-16531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please share your code which is executing the above command to analyze. you could try waitFor() function of Process process.waitFor() after executing the command.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '12, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/97e620804d00012d2cec1885d6422a13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manojdeoli&#39;s gravatar image" /><p><span>manojdeoli</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manojdeoli has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-16531" class="comments-container"></div><div id="comment-tools-16531" class="comment-tools"></div><div class="clear"></div><div id="comment-16531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

