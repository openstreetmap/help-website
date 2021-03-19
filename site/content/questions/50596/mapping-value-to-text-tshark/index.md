+++
type = "question"
title = "Mapping value to text tshark"
description = '''Hello, Is it possible in tshark to directly convert value to exact meaning text? I need similary like as: &quot;tshark -r pcap -V&quot; but I need it only on exact fields. For example:  tshark -r smpp.pcap -T fields -e smpp.command_id 0x80000015 0x80000004 0x00000004 0x80000004 0x00000004  Now I need to chang...'''
date = "2016-03-01T00:52:00Z"
lastmod = "2016-07-20T13:49:00Z"
weight = 50596
keywords = [ "mapping", "convert", "tshark", "value", "value_string" ]
aliases = [ "/questions/50596" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping value to text tshark](/questions/50596/mapping-value-to-text-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50596-score" class="post-score" title="current number of votes">0</div><span id="post-50596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Is it possible in tshark to directly convert value to exact meaning text? I need similary like as: "<code>tshark -r pcap -V</code>" but I need it only on exact fields.</p><p>For example: <code>tshark -r smpp.pcap -T fields -e smpp.command_id</code></p><pre><code>0x80000015
0x80000004
0x00000004
0x80000004
0x00000004</code></pre><p>Now I need to change to correct text like as (Submit_sm,Deliver_sm,and so on..) Something like <code>tshark -e _ws.col.Info</code> but I need it per argument for example <code>_ws.col.smpp.command_id</code>? Don't focus on protocol; I need it globally for a lot of different protocols.</p><p>Thanks a lot. Regards, Peter</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-value" rel="tag" title="see questions tagged &#39;value&#39;">value</span> <span class="post-tag tag-link-value_string" rel="tag" title="see questions tagged &#39;value_string&#39;">value_string</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '16, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/27f342105bd97d406c2c2ba2a5f164bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zuvo&#39;s gravatar image" /><p><span>zuvo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zuvo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jul '16, 13:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-50596" class="comments-container"></div><div id="comment-tools-50596" class="comment-tools"></div><div class="clear"></div><div id="comment-50596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54208"></span>

<div id="answer-container-54208" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54208-score" class="post-score" title="current number of votes">1</div><span id="post-54208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zuvo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To achieve this, you could try explicitly specifing the exact columns that you want to be displayed. For example, this will display the frame number and <code>smpp.command_id</code> for SMPP matching frames:</p><p><strong>On *nix:</strong></p><pre><code>tshark -o &#39;gui.column.format:&quot;No.&quot;,&quot;%m&quot;,&quot;SMPP Commmand ID&quot;,&quot;%Cus:smpp.command_id&quot;&#39; -Y &quot;smpp&quot; -r smpp.cap</code></pre><p><strong>On Windows:</strong></p><pre><code>tshark.exe -o &quot;gui.column.format:\&quot;No.\&quot;,\&quot;%m\&quot;,\&quot;SMPP Command ID\&quot;,\&quot;%Cus:smpp.command_id\&quot;&quot; -Y &quot;smpp&quot; -r smpp.cap</code></pre><p>Sample output:</p><pre><code> 4 Bind_transmitter
 5 Bind_transmitter - resp
 7 Enquire_link
 8 Enquire_link - resp
 9 Submit_sm
10 Submit_sm - resp
12 Unbind
13 Unbind - resp</code></pre><p>You can display just about any field using <code>%Cus</code>. For the so-called "built-in" fields, run <code>tshark -G column-formats</code> to see the specifiers needed (such as <code>%m</code> for the frame number in the example above).</p><p>You can also just run Wireshark and configure the columns you want there and then run <code>tshark</code> without the need to specify the columns, since <code>tshark</code> will just use the Wireshark-configured columns by default.</p><p>If you only want to use <em>some</em> of Wireshark's configured columns, you can pick and choose the ones you want using the <code>-T fields -e field1 -e field2 ...</code> syntax, specifying <code>-e _ws.col.Operation</code> for the SMPP Operation/Command ID field, "Operation" being the default name of the column when you right-click the field in Wireshark and choose, <em>"Apply as column"</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '16, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54208" class="comments-container"></div><div id="comment-tools-54208" class="comment-tools"></div><div class="clear"></div><div id="comment-54208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

