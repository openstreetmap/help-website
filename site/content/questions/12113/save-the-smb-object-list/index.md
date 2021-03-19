+++
type = "question"
title = "Save the SMB object list?"
description = '''If I invoke &quot;File-&amp;gt;Export-&amp;gt;Objects-&amp;gt;SMB&quot;, it brings up a pop-up window with a list of SMB objects. Is there a way to save this list? There are &quot;Save...&quot; buttons on the pop-up window, but these save the SMB objects themselves, not the list. I&#x27;d like to generate a report for SMB objects simil...'''
date = "2012-06-21T11:49:00Z"
lastmod = "2012-09-10T04:20:00Z"
weight = 12113
keywords = [ "save", "export", "smb" ]
aliases = [ "/questions/12113" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Save the SMB object list?](/questions/12113/save-the-smb-object-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12113-score" class="post-score" title="current number of votes">0</div><span id="post-12113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I invoke "File-&gt;Export-&gt;Objects-&gt;SMB", it brings up a pop-up window with a list of SMB objects. Is there a way to save this list? There are "Save..." buttons on the pop-up window, but these save the SMB objects themselves, not the list. I'd like to generate a report for SMB objects similar to the Statistics-&gt;HTTP-&gt;Requests... menu item.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '12, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/36573d2ce601b9b6310206cb7866a510?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jhand&#39;s gravatar image" /><p><span>jhand</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jhand has no accepted answers">0%</span></p></div></div><div id="comments-container-12113" class="comments-container"></div><div id="comment-tools-12113" class="comment-tools"></div><div class="clear"></div><div id="comment-12113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12116"></span>

<div id="answer-container-12116" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12116-score" class="post-score" title="current number of votes">1</div><span id="post-12116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no way to export the list from that GUI element.</p><p><strong>HOWEVER</strong>, you can try this:</p><blockquote><p><code>tshark.exe -r smb.cap -R "smb.cmd eq 0xa2 and smb.nt_status eq 0x0 and smb.alloc_size &gt;0"  -T fields -e ip.src -e smb.file -e smb.alloc_size</code><br />
</p></blockquote><p>This will output something like this:</p><blockquote><p><code>192.168.1.100 \\data\\file.dat 2609152</code><br />
<code>192.168.1.100 \\data\\file.dat 2609152</code><br />
<code>192.168.1.100 \\data\\test.txt  112</code><br />
<code>192.168.1.100 \\data\\test.txt  112</code><br />
<code>192.168.1.100 \\data\\test.txt  112</code><br />
<code>192.168.1.100 \\data\\test.txt  112</code><br />
</p></blockquote><p>Unfortunately, there are multiple similar lines of output, but you can easily filter that with <code>sort -u</code> (on unix) or similar tools on windows.</p><p>If that output is not exactly what you are looking for, the tshark command should at least get you started ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '12, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '12, 22:32</strong> </span></p></div></div><div id="comments-container-12116" class="comments-container"><span id="14154"></span><div id="comment-14154" class="comment"><div id="post-14154-score" class="comment-score"></div><div class="comment-text"><p>Hi, I want to save the resulting files with this command, how to register? when i export with wireshark,my file cant be save. wireshark say : "PIPE not implemented 0/0w 0% " " 0bytes " but tshark return the size.</p><p>how can I save files with a tshark?</p><p>Thank for your return</p></div><div id="comment-14154-info" class="comment-info"><span class="comment-age">(10 Sep '12, 01:17)</span> <span class="comment-user userinfo">sacabiaire</span></div></div><span id="14162"></span><div id="comment-14162" class="comment"><div id="post-14162-score" class="comment-score"></div><div class="comment-text"><p>That tsahrk command was only meant to get a list of the file names, not the files! If you need the files, go to:</p><blockquote><p><code>File -&gt; Export Objects -&gt; SMB</code></p></blockquote></div><div id="comment-14162-info" class="comment-info"><span class="comment-age">(10 Sep '12, 04:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12116" class="comment-tools"></div><div class="clear"></div><div id="comment-12116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

