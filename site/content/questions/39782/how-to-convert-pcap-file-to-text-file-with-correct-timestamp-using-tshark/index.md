+++
type = "question"
title = "How to convert pcap file to text file with correct timestamp using tshark ?"
description = '''What are the tshark options to be used to read/convert a pcap file to a text file, with its default one-line description, but with correct timestamps ? It increments from 0.0 by default, but I want the exact unix time for each of the packets in the text file along with the default values. I&#x27;m using ...'''
date = "2015-02-10T14:01:00Z"
lastmod = "2015-02-11T06:15:00Z"
weight = 39782
keywords = [ "tshark" ]
aliases = [ "/questions/39782" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to convert pcap file to text file with correct timestamp using tshark ?](/questions/39782/how-to-convert-pcap-file-to-text-file-with-correct-timestamp-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39782-score" class="post-score" title="current number of votes">0</div><span id="post-39782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What are the tshark options to be used to read/convert a pcap file to a text file, with its default one-line description, but with correct timestamps ?</p><p>It increments from 0.0 by default, but I want the exact unix time for each of the packets in the text file along with the default values.</p><p>I'm using the below command currently</p><p>tshark -i - &lt; srcfile.cap &gt; destfile.txt</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/28c650ab8536222f4cf246389571a94f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mlnsharma&#39;s gravatar image" /><p><span>mlnsharma</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mlnsharma has no accepted answers">0%</span></p></div></div><div id="comments-container-39782" class="comments-container"></div><div id="comment-tools-39782" class="comment-tools"></div><div class="clear"></div><div id="comment-39782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39786"></span>

<div id="answer-container-39786" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39786-score" class="post-score" title="current number of votes">1</div><span id="post-39786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mlnsharma has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What <span>@Jasper</span> said, or use the tshark CLI options, see <code>tshark -h</code>:</p><pre><code>-t a|ad|d|dd|e|r|u|ud    output format of time stamps (def: r: rel. to first)</code></pre><p>so, <code>tshark -r srcfile.pcap -t ad &gt; destfile.txt</code> will do the trick.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 16:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39786" class="comments-container"><span id="39795"></span><div id="comment-39795" class="comment"><div id="post-39795-score" class="comment-score"></div><div class="comment-text"><p>I wanted it in tshark only, not the GUI and this works. Thanks !</p></div><div id="comment-39795-info" class="comment-info"><span class="comment-age">(11 Feb '15, 06:15)</span> <span class="comment-user userinfo">mlnsharma</span></div></div></div><div id="comment-tools-39786" class="comment-tools"></div><div class="clear"></div><div id="comment-39786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39785"></span>

<div id="answer-container-39785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39785-score" class="post-score" title="current number of votes">1</div><span id="post-39785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Change the time column display format in the default preferences, e.g. by running Wireshark and using Edit -&gt; Preferences -&gt; User Interface -&gt; Columns. Set "Time" value to "Absolute Date and Time" (or any other time format you like).</p><p>tshark uses the default profile by default (no pun intended), so whatever you set in that profile is going to be used by tshark (unless you force a different profile setting via command line parameter)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39785" class="comments-container"></div><div id="comment-tools-39785" class="comment-tools"></div><div class="clear"></div><div id="comment-39785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

