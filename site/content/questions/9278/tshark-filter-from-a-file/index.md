+++
type = "question"
title = "tshark filter from a file"
description = '''Hi, I&#x27;m using tshark to capture hostnames (http.host), source (ip.src) and destination (ip.dst) IP&#x27;s, and the frame time (frame.time). I am capturing only tcp ports 80 and 443 (web traffic). The command I&#x27;m using is: tshark tcp port 80 or tcp port 443 -V -R &quot;http.request&quot; -Tfields -e http.host -e ip...'''
date = "2012-02-29T07:01:00Z"
lastmod = "2012-03-02T22:02:00Z"
weight = 9278
keywords = [ "filter", "tshark", "file" ]
aliases = [ "/questions/9278" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark filter from a file](/questions/9278/tshark-filter-from-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9278-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using tshark to capture hostnames (http.host), source (ip.src) and destination (ip.dst) IP's, and the frame time (frame.time). I am capturing only tcp ports 80 and 443 (web traffic). The command I'm using is: tshark tcp port 80 or tcp port 443 -V -R "http.request" -Tfields -e http.host -e ip.src -e ip.dst -e frame.time</p><p>Is there a way for me to pass a list of hostnames that I want to capture from a file? I understand that I could save the entire capture to a file and use grep -f to filter it after the fact. I am trying to avoid saving the entire capture to a file, and only save the hostnames that I'm interested in.<br />
</p><p>For example, I have a file called interesteddomains that contains a list of domains (i.e. <a href="http://facebook.com">facebook.com</a>, <a href="http://ebay.com">ebay.com</a>, etc.). These domains are listed on separate lines of this file. I want to pass this list of domains (from the file) to tshark, and only capture domains that are in this file.</p><p>I'm trying to pipe the realtime capture to grep, but it doesn't seem to like that (or I'm doing something wrong :)). I was wondering if I could eliminate the need to grep it and just handle the filtering in the tshark command.</p><p>Any help would be appreciated! I apologize if this is confusing.<br />
</p><p>Jason</p></div><div id="question-tags" class="tags-container tags">filter tshark file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '12, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/089dde95402bfa380543db12413c4855?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbloink&#39;s gravatar image" /><p>jbloink<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbloink has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-9278" class="comments-container"></div><div id="comment-tools-9278" class="comment-tools"></div><div class="clear"></div><div id="comment-9278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9302"></span>

<div id="answer-container-9302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9302-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is probably some complicated awk script that you can run to build a display filter from the contents of the file. Something like:</p><pre><code>cat domains.txt | awk &#39;{printf(&quot; http.host==\\&quot;%s\\&quot; &amp;&amp; &quot;, $1)}&#39;</code></pre><p>Punctuation soup! It should produce the following (assuming <a href="http://www.yahoo.com">www.yahoo.com</a> and <a href="http://www.facebook.com">www.facebook.com</a> are lines in that file):</p><pre><code>http.host==&quot;www.yahoo.com&quot; &amp;&amp;  http.host==&quot;www.facebook.com&quot; &amp;&amp;</code></pre><p>Starting to look like a tshark -R display filter? That's as close I could come given a few moments, but some combination of that, and using the backticks operator in bash might get you closer.<br />
</p><p>Alternately, you could whip up a quick perl or ruby script to parse the file, and output the display filter. Assuming such a magic script existed, you could build that filter like this:</p><pre><code>tshark [your options] -R &quot;`./magic-script.rb domains.txt` &amp;&amp; http.request&quot; -T fields -e [etc...]</code></pre><p>Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '12, 20:44</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p>zachad<br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '12, 20:44</p></div></div><div id="comments-container-9302" class="comments-container"><span id="9397"></span><div id="comment-9397" class="comment"><div id="post-9397-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys! I appreciate your help. I'll mess around a bit more and post any updates for future reference.</p><p>Jason</p></div><div id="comment-9397-info" class="comment-info"><span class="comment-age">(06 Mar '12, 07:53)</span> jbloink</div></div></div><div id="comment-tools-9302" class="comment-tools"></div><div class="clear"></div><div id="comment-9302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9322"></span>

<div id="answer-container-9322" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9322-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a> with the option -T fields to create a .csv file:<br />
$ tshark -r clmt\_04.pcap -T fields -e http.host | sort | uniq | sort &gt; http.host.csv<br />
$ tshark -r clmt\_04.pcap -T fields -e http.request.full\_uri | sort | uniq | sort &gt; http.request.full_uri.csv<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '12, 22:02</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-9322" class="comments-container"></div><div id="comment-tools-9322" class="comment-tools"></div><div class="clear"></div><div id="comment-9322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

