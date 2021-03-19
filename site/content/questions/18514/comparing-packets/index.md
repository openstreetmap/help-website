+++
type = "question"
title = "Comparing Packets"
description = '''I am looking for a way to do a &quot;stare and compare&quot; packet analysis. I have a situation with a SIP carrier who is sending an INVITE for a number that works and others that do not. They seem identical in format and such but I noticed that they were slightly different sizes (1109 for the one that worke...'''
date = "2013-02-11T15:11:00Z"
lastmod = "2015-03-19T11:45:00Z"
weight = 18514
keywords = [ "comparison", "packet" ]
aliases = [ "/questions/18514" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Comparing Packets](/questions/18514/comparing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18514-score" class="post-score" title="current number of votes">1</div><span id="post-18514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a way to do a "stare and compare" packet analysis. I have a situation with a SIP carrier who is sending an INVITE for a number that works and others that do not. They seem identical in format and such but I noticed that they were slightly different sizes (1109 for the one that worked and 1112 for the ones that don't work). Where they differ, however, is the problem. Is there a utility tool that is set up for this?</p><p>Thanks</p><p>Eric</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-comparison" rel="tag" title="see questions tagged &#39;comparison&#39;">comparison</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '13, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-18514" class="comments-container"></div><div id="comment-tools-18514" class="comment-tools"></div><div class="clear"></div><div id="comment-18514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="18515"></span>

<div id="answer-container-18515" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18515-score" class="post-score" title="current number of votes">0</div><span id="post-18515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When I have to do something like this I try to avoid doing "spot the difference" compares by viewing the traces side by side. I'd rather save the two frames in question into a separate trace (so that they're right next to each other) - this is easy to do by marking the two frames in question and then using "File -&gt; Export Specified Packets" and selecting "marked packets" in the selection box.</p><p>Then, you can just load this very short trace file and use cursor up/down to go back and forth between the two frames. By looking at the hex view you can see what bytes change right away, and after that check the decode for what they stand for.</p><p>If saving is too complicated you could also use the "Go back/forward in Packet History" buttons in the toolbar after having clicked on both packets in question, but if the distance is greater than a few frames it can be confusing.</p><p>As Hansang and I always say: the human eye is good in spotting changes more than staring at immobile text :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '13, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '13, 16:02</strong> </span></p></div></div><div id="comments-container-18515" class="comments-container"><span id="18542"></span><div id="comment-18542" class="comment"><div id="post-18542-score" class="comment-score"></div><div class="comment-text"><p>Jasper - thanks for your answer and that was where I was headed. The carrier insists they are sending the SIP invites the same way every time. The manufacturer insists that they are not. Neither seem all that willing to slug it out bit-by-bit with me (I'm willing!). So, I was looking for something that was more automated instead of me saying to one or the other "Here it is" versus a program/tool that would highlight an extra white space, character -- anything. They tend to be more receptive to that sort of thing. Tried WinDiff but that was not useful in this case. Thanks</p><p>Eric</p></div><div id="comment-18542-info" class="comment-info"><span class="comment-age">(12 Feb '13, 04:33)</span> <span class="comment-user userinfo">EricKnaus</span></div></div><span id="18546"></span><div id="comment-18546" class="comment"><div id="post-18546-score" class="comment-score"></div><div class="comment-text"><p>Sounds like you're trying to find a more automatic solution? If one compare sample is enough, you can do what <span>@kurt</span> suggests - use exporting to get ASCII representations and then diff them. If you need to compare tons of samples things get a lot more complicated...</p></div><div id="comment-18546-info" class="comment-info"><span class="comment-age">(12 Feb '13, 05:41)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="18550"></span><div id="comment-18550" class="comment"><div id="post-18550-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Sounds like you're trying to find a more automatic solution?</p></blockquote><p>The 'problem' is: It's not about comparing different pcap files (there are more/or less good ways to do that). It's about comparing packets (actually just the payload) within a single capture file. That's something you usually do not need, except for very special cases. I don't think there is any automatic solution 'out there' that does exactly that.</p></div><div id="comment-18550-info" class="comment-info"><span class="comment-age">(12 Feb '13, 06:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-18515" class="comment-tools"></div><div class="clear"></div><div id="comment-18515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18544"></span>

<div id="answer-container-18544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18544-score" class="post-score" title="current number of votes">0</div><span id="post-18544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but I noticed that they were slightly different sizes (1109 for the one that worked and 1112 for the ones that don't work). Where they differ, however, is the problem.</p></blockquote><p>Don't you see a difference if you look at the payload in HEX (possibly export the HEX output and let WinDiff find the difference).</p><p>Here is how I would do it.</p><ul><li>Select packet #1 (Size: 1109)</li><li>right click it</li><li><p>print -&gt; "Plain Text", "Output to file", only "packet bytes" (Packet format)</p></li><li><p>Select packet #2 (Size: 1102)</p></li><li>right click it</li><li>print -&gt; "Plain Text", "Output to file", only "packet bytes" (Packet format)</li></ul><p>Comapre the files with WinDiff or WinMerge. Ignore the first 40 bytes IP/TCP header (+/- 1 or 2 bytes depending on the header fields).</p><p>Now you should see a difference. If there is none, can you upload those two packets (or the HEX output) somewhere (google docs, one click file hoster, pastebin.com., etc. BEWARE the privacy issues in doing so!!).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-18544" class="comments-container"></div><div id="comment-tools-18544" class="comment-tools"></div><div class="clear"></div><div id="comment-18544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40693"></span>

<div id="answer-container-40693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40693-score" class="post-score" title="current number of votes">0</div><span id="post-40693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Save packets into their parsed textual representation:</p><p>File-&gt;Export packet dissections-&gt;(select format),in the save dialog specify the packets and "packet details" to include.</p><p>Then do a diff over the textual results</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '15, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/4d98e414a47934d66cb78bf73d0845ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="native_api&#39;s gravatar image" /><p><span>native_api</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="native_api has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Mar '15, 11:46</strong> </span></p></div></div><div id="comments-container-40693" class="comments-container"></div><div id="comment-tools-40693" class="comment-tools"></div><div class="clear"></div><div id="comment-40693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

