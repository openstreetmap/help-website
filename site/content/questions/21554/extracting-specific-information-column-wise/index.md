+++
type = "question"
title = "Extracting specific information column wise"
description = '''Hi i have a wire shark capture, in which there are specific information in each packet which i can see after decoding it as RTP. now i need those data into a csv file for further investigations. what is the procedure for getting those data in csv format. '''
date = "2013-05-29T02:34:00Z"
lastmod = "2013-05-31T02:21:00Z"
weight = 21554
keywords = [ "extract" ]
aliases = [ "/questions/21554" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting specific information column wise](/questions/21554/extracting-specific-information-column-wise)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21554-score" class="post-score" title="current number of votes">0</div><span id="post-21554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i have a wire shark capture, in which there are specific information in each packet which i can see after decoding it as RTP. now i need those data into a csv file for further investigations. what is the procedure for getting those data in csv format.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '13, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/6dd0cb59a3bcab4b6db4e6c3f8014ff4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pranav%20s&#39;s gravatar image" /><p><span>pranav s</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pranav s has no accepted answers">0%</span></p></div></div><div id="comments-container-21554" class="comments-container"></div><div id="comment-tools-21554" class="comment-tools"></div><div class="clear"></div><div id="comment-21554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21632"></span>

<div id="answer-container-21632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21632-score" class="post-score" title="current number of votes">1</div><span id="post-21632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand the question correctly, one approach might be to add the field of interest as a displayed column, and then export the dissected packets.</p><p>One way you can add any field as a column, is by finding the field in the packet details pane, right click it, and then select "Apply as column". Another, harder, way to do it is to select Edit | Preferences | Columns and make changes to the displayed columns from there.</p><p>You can export all the displayed columns, for specific trace records or for all records, by selecting File | Export Packet Dissections | and then select the export format you prefer (.csv, .txt, etc)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '13, 21:51</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p><span>griff</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span></p></div></div><div id="comments-container-21632" class="comments-container"><span id="21636"></span><div id="comment-21636" class="comment"><div id="post-21636-score" class="comment-score"></div><div class="comment-text"><p>You, sir, just saved me a ton of manual work. Have some points.</p></div><div id="comment-21636-info" class="comment-info"><span class="comment-age">(31 May '13, 00:24)</span> <span class="comment-user userinfo">spoorzoeker</span></div></div><span id="21642"></span><div id="comment-21642" class="comment"><div id="post-21642-score" class="comment-score"></div><div class="comment-text"><p>the type of data i am talking about is bit rate of video, in a single packet its shows latest and last 3 bit rate (as history). so in total there are 4 data with same name "Current Bit rate = a (b,c,d)" so when applying as column, the column shows 4 bit rate as a,b,c,d but i need only one in that column (the latest one)</p></div><div id="comment-21642-info" class="comment-info"><span class="comment-age">(31 May '13, 02:13)</span> <span class="comment-user userinfo">pranav s</span></div></div><span id="21643"></span><div id="comment-21643" class="comment"><div id="post-21643-score" class="comment-score"></div><div class="comment-text"><p>Then you can use the "occurrence" value. Pick 0 for all values, 1 for the first, 2 for the second etc. Or use -1 to always pick the last one regardless of how many values there are.</p></div><div id="comment-21643-info" class="comment-info"><span class="comment-age">(31 May '13, 02:21)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-21632" class="comment-tools"></div><div class="clear"></div><div id="comment-21632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21638"></span>

<div id="answer-container-21638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21638-score" class="post-score" title="current number of votes">1</div><span id="post-21638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One other way (especially if you need to do this on multiple files or multiple times) is to use tshark. You can use the following syntax:</p><pre><code>tshark -r &lt;file&gt; -d udp.port==&lt;port&gt;,rtp -T fields -e ip.src -e ip.dst -e &lt;field3&gt; -e &lt;field4&gt;</code></pre><p>You can change the header, separator etc, see tshark -h:</p><pre><code>  -E&lt;fieldsoption&gt;=&lt;value&gt; set options for output when -Tfields selected:
     header=y|n            switch headers on and off
     separator=/t|/s|&lt;char&gt; select tab, space, printable character as separator
     occurrence=f|l|a      print first, last or all occurrences of each field
     aggregator=,|/s|&lt;char&gt; select comma, space, printable character as
                           aggregator
     quote=d|s|n           select double, single, no quotes for values</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '13, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21638" class="comments-container"><span id="21639"></span><div id="comment-21639" class="comment"><div id="post-21639-score" class="comment-score"></div><div class="comment-text"><p>For field I can add any of the fields given in the list under Preferences | Column? Is this list exhaustive or are there more options I can find in a help function in the man pages somewhere but have not yet uncovered?</p></div><div id="comment-21639-info" class="comment-info"><span class="comment-age">(31 May '13, 01:14)</span> <span class="comment-user userinfo">spoorzoeker</span></div></div><span id="21640"></span><div id="comment-21640" class="comment"><div id="post-21640-score" class="comment-score"></div><div class="comment-text"><p>For "field" you can use any filterable field, click on the specific field of interest in the packet details pane and you will see the field name in the status bar (you might need to enlarge the left section). You can also use "rightclick -&gt; copy -&gt; fieldname" (or SHIFT-CTRL-F) to get the fieldname.</p></div><div id="comment-21640-info" class="comment-info"><span class="comment-age">(31 May '13, 01:19)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-21638" class="comment-tools"></div><div class="clear"></div><div id="comment-21638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

