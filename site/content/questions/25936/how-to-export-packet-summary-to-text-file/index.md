+++
type = "question"
title = "How to export packet summary to text file?"
description = '''I have a capture of HTTP traffic that I need to extract values of Info field from. If I right click on each packet, select Copy -&amp;gt; Summary (Text) and then paste it in notepad I would eventually get all the values, but it would take me hours to do. Is there a quicker way to do it? None of the expo...'''
date = "2013-10-12T08:11:00Z"
lastmod = "2013-10-14T18:25:00Z"
weight = 25936
keywords = [ "info", "field", "export" ]
aliases = [ "/questions/25936" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to export packet summary to text file?](/questions/25936/how-to-export-packet-summary-to-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25936-score" class="post-score" title="current number of votes">1</div><span id="post-25936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture of HTTP traffic that I need to extract values of Info field from. If I right click on each packet, select Copy -&gt; Summary (Text) and then paste it in notepad I would eventually get all the values, but it would take me hours to do. Is there a quicker way to do it? None of the exports I tried worked for me.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '13, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p><span>net_tech</span><br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Oct '13, 10:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-25936" class="comments-container"></div><div id="comment-tools-25936" class="comment-tools"></div><div class="clear"></div><div id="comment-25936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25937"></span>

<div id="answer-container-25937" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25937-score" class="post-score" title="current number of votes">2</div><span id="post-25937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="net_tech has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you you really want all the information from the Info column, then you are probably better off using <a href="http://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> for this. Something like:</p><pre><code>tshark -r file.pcap -P -Y &quot;http&quot; -o gui.column.format:&#39;&quot;Info&quot;, &quot;%i&quot;&#39; &gt; http_info.txt</code></pre><p>Otherwise, if you're just looking for specific http fields from specific http packets, then you might want to just extract those specific fields of interest. A hypothetical example:</p><pre><code>tshark -r file.pcap -Y &quot;http.request.method == GET&quot; -T fields -e frame.number -e http.request.uri -e http.user_agent ...</code></pre><p><strong><em>UPDATE</em></strong></p><p>I believe I made a mistake above in thinking that you only wanted the Info column, but I think you are interested in all columns, so all you really should need to do is to run <code>tshark</code> as follows (substituting "http" for whatever filter is desirable for you):</p><pre><code>tshark -r file.pcap -P -Y &quot;http&quot; &gt; http_summary.txt</code></pre><p>This will get you all of the columns that Wireshark is currently configured to display.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '13, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Oct '13, 10:30</strong> </span></p></div></div><div id="comments-container-25937" class="comments-container"><span id="25941"></span><div id="comment-25941" class="comment"><div id="post-25941-score" class="comment-score"></div><div class="comment-text"><p>cmaynard,</p><p>tshark -r file.pcap -P -Y "http" &gt; http_summary.txt is exactly what I was looking for! Thanks for your help.</p></div><div id="comment-25941-info" class="comment-info"><span class="comment-age">(12 Oct '13, 11:41)</span> <span class="comment-user userinfo">net_tech</span></div></div><span id="25983"></span><div id="comment-25983" class="comment"><div id="post-25983-score" class="comment-score"></div><div class="comment-text"><p>I should have also mentioned that you can accomplish the same thing just as easily with Wireshark using <code>File -&gt; Export Packet Dissections -&gt; as "Plain Text" file...</code>, and then just be sure to select "Packet summary line" and deselect all other options in the "Packet Format" grouping.</p><p>My initial misinterpretation of the question led me to direct you to use tshark, which is why I forgot to mention the Wireshark method, but as you can see, you can accomplish this with either Wireshark or tshark.</p></div><div id="comment-25983-info" class="comment-info"><span class="comment-age">(14 Oct '13, 18:25)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-25937" class="comment-tools"></div><div class="clear"></div><div id="comment-25937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

