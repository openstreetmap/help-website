+++
type = "question"
title = "How to split captured traffic into multiple files depending on the delay between packets using tshark"
description = '''Dear All, I want to split captured traffic based on the delay between packet. so that if the the delay between two packet is more than the threshold, save the trace in new file. How can I do it using tshark commands? Edit1:  here is the code I use for splitting traffic based on Sindy&#x27;s answer:  end=...'''
date = "2016-09-02T15:00:00Z"
lastmod = "2016-09-03T02:35:00Z"
weight = 55309
keywords = [ "pcapng", "mate", "tshark" ]
aliases = [ "/questions/55309" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to split captured traffic into multiple files depending on the delay between packets using tshark](/questions/55309/how-to-split-captured-traffic-into-multiple-files-depending-on-the-delay-between-packets-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55309-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All,</p><p>I want to split captured traffic based on the delay between packet. so that if the the delay between two packet is more than the threshold, save the trace in new file.</p><p>How can I do it using tshark commands?</p><p>Edit1:</p><p>here is the code I use for splitting traffic based on Sindy's answer:</p><pre><code>    end=true
    id=1
    while $end
    do 
        tshark -r $trace -o mate.config:/home/zaha/Documents/mate.config -Y &quot;mate.burst == $id&quot; -w capture/flows/${nbase}/mainflow/${base}_$id.pcapng
        if [ -s capture/flows/${nbase}/mainflow/${base}_$id.pcapng ]; then
            id=$[$id +1]
        else
            end=false
        fi
    done</code></pre><p>And use Sindy's MATE configuration with just changing the delay time.</p><p>But while loop didn't stop. should I use other option to check whether .pcapng file is empty or not?</p></div><div id="question-tags" class="tags-container tags">pcapng mate tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '16, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/1595a24111dff7d0376d456e91895399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zahra&#39;s gravatar image" /><p>Zahra<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zahra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Sep '16, 06:40</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55309" class="comments-container"></div><div id="comment-tools-55309" class="comment-tools"></div><div class="clear"></div><div id="comment-55309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55312"></span>

<div id="answer-container-55312" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55312-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I get you right and you want to create a new file each time the pause between packets is longer than the threshold, it cannot be done while capturing. <a href="https://wiki.wireshark.org/Mate/Manual">MATE</a> could be a way to mark all frames belonging to the same "burst" with a unique numeric ID (<code>mate.burst</code> in the example code below), allowing you to filter the capture file on that ID and write the result for each ID into its own file, maybe using a script incrementing the ID and calling <code>tshark -r my_capture.pcap -Y "mate.burst == $id" -w my_capture_$id.pcap</code> in a loop until the output file becomes empty.</p><p>An example of MATE configuration with a gap threshold of 0.01 second follows:</p><pre><code> Transform make_start {
   Match (delay&gt;0.01) Insert (start_flag);
   Match (number=1) Insert (start_flag);
 };

 Transform set_all_to_0 {
   Match (number) Replace (number=0);
 };

 Pdu any_frame Proto frame Transport mate {
   Extract delay From frame.time_delta;
   Extract number From frame.number;
   Transform make_start, set_all_to_0;
 };

 Gop burst On any_frame Match (number) {
   Start (start_flag);
 };

 Done;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '16, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Sep '16, 23:54</p></div></div><div id="comments-container-55312" class="comments-container"><span id="55316"></span><div id="comment-55316" class="comment"><div id="post-55316-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply, I want to do it after capturing, while reading traffic using -r and other filtering options in my processing phase. Is there other solution?</p></div><div id="comment-55316-info" class="comment-info"><span class="comment-age">(03 Sep '16, 03:37)</span> Zahra</div></div><span id="55317"></span><div id="comment-55317" class="comment not_top_scorer"><div id="post-55317-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I want to do it after capturing</p></blockquote><p>Well, I've already described the suggestion as only applicable in the post-processing mode, so I'm not sure whether I get your reaction properly.</p><p>If you want to split the capture into parts up to the gaps between frames only after applying your display filter, I'm afraid you would have to use two instances of tshark in a chain. Tshark does support an idea of a separate "read filter" and "display filter" which use the same syntax but serve a different purpose, yet the two-pass mode of tshark which is currently mandatory for use of read filter has some trouble with MATE. But you may give it a try:</p><pre><code>tshark -r my_capture.pcap -2 -R &quot;your_filter_expression&quot; -Y &quot;mate.burst == N&quot; -w my_capture_N.pcap</code></pre><p>If it does not work, you have to revert to the chain method:</p><pre><code>tshark -r my_capture.pcap -Y &quot;your_filter_expression&quot; -w - | tshark -r - -Y &quot;mate.burst == N&quot; -w my_capture_N.pcap</code></pre><p>But it may not be possible on Windows.</p></div><div id="comment-55317-info" class="comment-info"><span class="comment-age">(03 Sep '16, 03:51)</span> sindy</div></div><span id="55318"></span><div id="comment-55318" class="comment not_top_scorer"><div id="post-55318-score" class="comment-score"></div><div class="comment-text"><p>Sorry I didn't try MATE before, how should I add MATE configuration to my bash script. In <a href="https://wiki.wireshark.org/Mate/GettingStarted">https://wiki.wireshark.org/Mate/GettingStarted</a> wasn't any explanation for do it in ubuntu and also in bash script. Could you plz help me in this?</p></div><div id="comment-55318-info" class="comment-info"><span class="comment-age">(03 Sep '16, 09:02)</span> Zahra</div></div><span id="55320"></span><div id="comment-55320" class="comment"><div id="post-55320-score" class="comment-score">1</div><div class="comment-text"><p>tshark shares a common preferences file with Wireshark, so you can use Wireshark's GUI to set the MATE configuration file. But you can use <code>-o preference:value</code> to override any of the values stored in the preferences file, so for our case, it would be <code>-o mate.config:/full/path/to/your/mate/config/file</code></p></div><div id="comment-55320-info" class="comment-info"><span class="comment-age">(03 Sep '16, 11:47)</span> sindy</div></div><span id="55321"></span><div id="comment-55321" class="comment not_top_scorer"><div id="post-55321-score" class="comment-score"></div><div class="comment-text"><p>thanks, now tshark works fine, but there is a problem about check file is empty or not?</p></div><div id="comment-55321-info" class="comment-info"><span class="comment-age">(03 Sep '16, 13:09)</span> Zahra</div></div><span id="55322"></span><div id="comment-55322" class="comment"><div id="post-55322-score" class="comment-score">1</div><div class="comment-text"><p>The thing is that for a pcap or pcapng file, "empty" means "contains no frames", not "has zero size", so <code>-s filename</code> returns true even for empty files. The reason is that tshark creates the file and writes the header into it right at start, not as late as when writing the first frame. For pcap, the size of an empty file is 24 bytes; for pcapng, it is <del>128 bytes</del> variable depending on the environment.</p><p>Google of "file size bash" returns links to several Q&amp;A sites with sophisticated answers; I would myself use <code>wc -c &lt; filename</code>. So the whole replacement of <code>if [ -s capture/flows/${nbase}/mainflow/${base}_$id.pcapng ] ;</code> in your script would be <code>if (($(wc -c &lt; capture/flows/${nbase}/mainflow/${base}_$id.pcapng)&gt;128)) ;</code></p></div><div id="comment-55322-info" class="comment-info"><span class="comment-age">(03 Sep '16, 23:34)</span> sindy</div></div><span id="55323"></span><div id="comment-55323" class="comment not_top_scorer"><div id="post-55323-score" class="comment-score"></div><div class="comment-text"><p>in my case empty pcapng file is 380, is there any differences by case?</p></div><div id="comment-55323-info" class="comment-info"><span class="comment-age">(03 Sep '16, 23:55)</span> Zahra</div></div><span id="55324"></span><div id="comment-55324" class="comment"><div id="post-55324-score" class="comment-score">1</div><div class="comment-text"><p>I haven't analysed it deeply, but it depends on what tshark writes to the file at start. If the interface description(s) are written, the resulting size depends on the interface name(s) which are strings whose size depends on the environment. Just for the fun of it, can you post your empty pcapng file?</p><p>It seems that tshark has no option allowing to easily evaluate emptiness of a file, nor the manual says anything about a return code.</p><p>So to make the script portable, you may have to use a never matching display filter like <code>-Y "eth and !eth"</code> to generate an output file which is surely empty and use its size as a reference for the comparison.</p></div><div id="comment-55324-info" class="comment-info"><span class="comment-age">(04 Sep '16, 00:16)</span> sindy</div></div><span id="55325"></span><div id="comment-55325" class="comment not_top_scorer"><div id="post-55325-score" class="comment-score"></div><div class="comment-text"><p>thanks, here is my empty .pcapng file. <a href="http://s000.tinyupload.com/?file_id=03339871074200476632">http://s000.tinyupload.com/?file_id=03339871074200476632</a></p></div><div id="comment-55325-info" class="comment-info"><span class="comment-age">(04 Sep '16, 00:31)</span> Zahra</div></div><span id="55327"></span><div id="comment-55327" class="comment"><div id="post-55327-score" class="comment-score">1</div><div class="comment-text"><p>OK, so the size of an "empty" pcapng really depends on a lot of factors, not just on the environment where tshark runs.</p><ul><li><p>in my case, there is just the signature of the application which has created it, which was tshark because the input file was a pcap one, not a pcapng one.</p></li><li><p>in your case, the original creator of the pcapng was dumpcap, so on top of its signature, there is also an interface description and capture filter because tshark has copied all this information from the input file to the output one.</p></li></ul></div><div id="comment-55327-info" class="comment-info"><span class="comment-age">(04 Sep '16, 01:04)</span> sindy</div></div></div><div id="comment-tools-55312" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-55312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

