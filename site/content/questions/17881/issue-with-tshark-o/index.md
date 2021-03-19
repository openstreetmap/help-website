+++
type = "question"
title = "Issue with tshark -o"
description = '''Hai, I am trying to capture packets using tshark from JAVA (OS: Ubuntu). From terminal i can run below command successfully. tshark -i any -o column.format:&quot;&quot;source&quot;, &quot;%s&quot;, &quot;srcport&quot;, &quot;%uS&quot;&quot; -f &quot;port 80 or port 443&quot; But from JAVA its throwing below message  tshark: Invalid -o flag &quot;column.format:&quot;&quot;s...'''
date = "2013-01-22T22:59:00Z"
lastmod = "2013-01-24T01:29:00Z"
weight = 17881
keywords = [ "-o", "tshark" ]
aliases = [ "/questions/17881" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Issue with tshark -o](/questions/17881/issue-with-tshark-o)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17881-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hai,</p><p>I am trying to capture packets using tshark from JAVA (OS: Ubuntu).</p><p>From terminal i can run below command successfully. tshark -i any -o column.format:""source", "%s", "srcport", "%uS"" -f "port 80 or port 443"</p><p>But from JAVA its throwing below message tshark: Invalid -o flag "column.format:""source","</p><p>But i can invoke commands like "tshark -i any" from java with out any issues. Is there any other thing i need to correct to get the exact output from JAVA. Please Help...</p></div><div id="question-tags" class="tags-container tags">-o tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '13, 22:59</strong></p><img src="https://secure.gravatar.com/avatar/88882b8f308c0d54b3934a26b2b3aac4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Krishnaprasad&#39;s gravatar image" /><p>Krishnaprasad<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Krishnaprasad has no accepted answers">0%</span></p></div></div><div id="comments-container-17881" class="comments-container"></div><div id="comment-tools-17881" class="comment-tools"></div><div class="clear"></div><div id="comment-17881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17919"></span>

<div id="answer-container-17919" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17919-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem why your Java application reports an invalid -o flag is because the version of the <a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/lang/Runtime.html#exec(java.lang.String)">Runtime.exec</a> method is responsible for splitting the supplied string into separate command line arguments. By default, this method uses the space, tab, newline, carriage-return and the form-feed characters. So as you can see, because there is a white space character between [column.format:\"\"source\",] [\"%s\",], this version of the exec method treats them as 2 distinct arguments.</p><p>The solution will be to use the other version of the <a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/lang/Runtime.html#exec(java.lang.String%5B%5D)">Runtime.exec</a> method which takes the system command and arguments in as an array parameter. You can therefore manually split out the command line arguments and define them as separate strings in the array parameter as follows:</p><p><code>Process proc = Runtime.getRuntime().exec(new String[] { "tshark",    "-i", "any",    "-o", "column.format:\"source\", \"%s\", \"srcport\", \"%uS\"",    "-f", "port 80 or port 443"});</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/b5ccb6961561257073b2910290dc97b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeff%20Moszuti&#39;s gravatar image" /><p>Jeff Moszuti<br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeff Moszuti has one accepted answer">100%</span></p></div></div><div id="comments-container-17919" class="comments-container"><span id="17927"></span><div id="comment-17927" class="comment"><div id="post-17927-score" class="comment-score"></div><div class="comment-text"><p>Excellent, It worked..... Thanks a ton :)</p></div><div id="comment-17927-info" class="comment-info"><span class="comment-age">(24 Jan '13, 04:27)</span> Krishnaprasad</div></div><span id="18270"></span><div id="comment-18270" class="comment"><div id="post-18270-score" class="comment-score"></div><div class="comment-text"><p>Its not related to tshark but if some one can help me with this issue that will be great...</p><p><a href="http://stackoverflow.com/questions/14680942/how-to-pass-the-terminal-output-to-java-text-area-while-its-apperaing-in-termina">http://stackoverflow.com/questions/14680942/how-to-pass-the-terminal-output-to-java-text-area-while-its-apperaing-in-termina</a></p></div><div id="comment-18270-info" class="comment-info"><span class="comment-age">(03 Feb '13, 21:40)</span> Krishnaprasad</div></div></div><div id="comment-tools-17919" class="comment-tools"></div><div class="clear"></div><div id="comment-17919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17882"></span>

<div id="answer-container-17882" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17882-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But from JAVA its throwing below message tshark: Invalid -o flag "column.format:""source","</p></blockquote><p>That's a problem with the quotes. You need to escape them with \.</p><blockquote><p><code>.exec("tshark -i any -o column.format:\"\" ...</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '13, 23:56</p></div></div><div id="comments-container-17882" class="comments-container"><span id="17885"></span><div id="comment-17885" class="comment"><div id="post-17885-score" class="comment-score"></div><div class="comment-text"><h1 id="kurt">@Kurt</h1><p>Thanks for your reply.</p><p>I did the same here is the complete code, its not working. If i tried the same from terminal its working..</p><p>====</p><pre><code>String[] cmdArray = {&quot;tshark -i any -o column.format:\&quot;\&quot;source\&quot;, \&quot;%s\&quot;, \&quot;srcport\&quot;, \&quot;%uS\&quot;\&quot; -f \&quot;port 80 or port 443\&quot;&quot;};
     for (String cmd: cmdArray) 
    {
        System.out.println(&quot;Executing command : &quot;+cmd);
        try
        {
            Process proc = Runtime.getRuntime().exec(cmd); 
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String str = in.readLine();
            while(str != null)
            {
                System.out.println(str);
                //  res += str + &quot;\n&quot;;
                str = in.readLine();
            }
            in.close();

            BufferedReader in2 = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
            String str1 = in2.readLine();
            while(str1 != null)
            {
                System.out.println(&quot;Inside getErrorStream &quot;+str1);
                //  res += str + &quot;\n&quot;;
                str1 = in2.readLine();
            }
            in2.close();

            proc.waitFor();
            System.out.println(&quot;Exit value is : &quot;+proc.exitValue());
            proc.destroy();
        }
        catch(IOException | InterruptedException e)
        {
            System.out.println(&quot;Exception on CommandExc class :&quot; + e.toString());
                            e.printStackTrace();
        }
    } //end of for</code></pre><p>====</p><p>Thanks</p></div><div id="comment-17885-info" class="comment-info"><span class="comment-age">(22 Jan '13, 23:35)</span> Krishnaprasad</div></div><span id="17889"></span><div id="comment-17889" class="comment"><div id="post-17889-score" class="comment-score"></div><div class="comment-text"><p>O.K. So do you get the same <strong>error</strong> now, or can't you read the output of the command?</p><p>If it's the same error, please try this:</p><p><code>String[] cmdArray = {"tshark -i any -o column.format:\"source, %s, srcport, %uS\" -f \"port 80 or port 443\""};</code><br />
</p><p>or this:</p><p><code>String[] cmdArray = {"tshark -i any -o column.format:'source, %s, srcport, %uS' -f 'port 80 or port 443'"};</code></p></div><div id="comment-17889-info" class="comment-info"><span class="comment-age">(22 Jan '13, 23:45)</span> Kurt Knochner ♦</div></div><span id="17892"></span><div id="comment-17892" class="comment"><div id="post-17892-score" class="comment-score"></div><div class="comment-text"><p>Hai Kurt,</p><p>No Luck I tried both i.e</p><pre><code>String[] cmdArray = {&quot;tshark -i any -o column.format:\&quot;source, %s, srcport, %uS\&quot; -f \&quot;port 80 or port 443\&quot;&quot;};</code></pre><p>AND this:</p><pre><code>String[] cmdArray = {&quot;tshark -i any -o column.format:&#39;source, %s, srcport, %uS&#39; -f &#39;port 80 or port 443&#39;&quot;};</code></pre><p>== Message</p><pre><code>[email protected]:~/Desktop/java/pgms/cmd$ javac CommandExc.java [email protected]:~/Desktop/java/pgms/cmd$ java CommandExc

Executing command : tshark -i any -o column.format:&quot;source, %s, srcport, %uS&quot; -f &quot;port 80 or port 443&quot;

Inside getErrorStream tshark: **Invalid -o flag &quot;column.format:&quot;source,&quot;**

Exit value is : 1

[email protected]:~/Desktop/java/pgms/cmd$ javac CommandExc.java [email protected]:~/Desktop/java/pgms/cmd$ java CommandExc

Executing command : tshark -i any -o column.format:&#39;source, %s, srcport, %uS&#39; -f &#39;port 80 or port 443&#39;

Inside getErrorStream tshark: **Invalid -o flag &quot;column.format:&#39;source,&quot;**

Exit value is : 1

[email protected]:~/Desktop/java/pgms/cmd$</code></pre></div><div id="comment-17892-info" class="comment-info"><span class="comment-age">(23 Jan '13, 00:48)</span> Krishnaprasad</div></div></div><div id="comment-tools-17882" class="comment-tools"></div><div class="clear"></div><div id="comment-17882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

