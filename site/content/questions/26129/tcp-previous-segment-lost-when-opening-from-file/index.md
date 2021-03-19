+++
type = "question"
title = "TCP previous segment lost when opening from file"
description = '''I am trying to save a dump, and load it on a similar wireshark. I am also copying the .wireshark directory to the other machine. However, HTTP/XML packets are transformed to &quot;Continuation or non-HTTP traffic&quot;. Any ideas?  edit Saved packets were saved in the following way:  marked packets of interes...'''
date = "2013-10-17T07:21:00Z"
lastmod = "2013-10-18T02:48:00Z"
weight = 26129
keywords = [ "prev_seg_lost" ]
aliases = [ "/questions/26129" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP previous segment lost when opening from file](/questions/26129/tcp-previous-segment-lost-when-opening-from-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26129-score" class="post-score" title="current number of votes">0</div><span id="post-26129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to save a dump, and load it on a similar wireshark. I am also copying the .wireshark directory to the other machine. However, HTTP/XML packets are transformed to "Continuation or non-HTTP traffic". Any ideas?</p><hr /><h2 id="edit">edit</h2><p>Saved packets were saved in the following way:</p><ul><li>marked packets of interest</li><li>save -&gt; Marked packets only</li></ul><p>Saving displayed packets also does not work as expected.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-prev_seg_lost" rel="tag" title="see questions tagged &#39;prev_seg_lost&#39;">prev_seg_lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '13, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/7988f36d0ee9050e8f1d646db55a9eb0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pihentagy&#39;s gravatar image" /><p><span>pihentagy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pihentagy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Oct '13, 01:53</strong> </span></p></div></div><div id="comments-container-26129" class="comments-container"></div><div id="comment-tools-26129" class="comment-tools"></div><div class="clear"></div><div id="comment-26129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26135"></span>

<div id="answer-container-26135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26135-score" class="post-score" title="current number of votes">2</div><span id="post-26135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What exactly are you doing? The topic you use mentions "TCP previous segment lost", while your question text doesn't. So I'm doing an assumption here, and you can correct me if I am wrong:</p><p>I guess that you try to save all packets that are marked "previous segment lost" to a file to just have the packets in one file where a segment was lost before each of them. Afterwards, the trace looks different, and instead of the packets you saw in the complete file you now get "Continuation or non-HTTP traffic".</p><p>If I'm guessing correctly then you are trying to do something that does not work. TCP expert messages like "previous segment lost" are diagnosed based on packet relationships, e.g. for lost segments Wireshark analyzes the TCP sequence numbers for gaps. It can only do that if it has both packets before and after the gap. So if you save just the packets with the diagnosis "previous segment lost" you only save the second packet, and when reopening the file, it will not have the diagnosis anymore - because Wireshark can do that without the first. Expert messages are not saved with frames, they are created on load.</p><p>Back to the HTTP problem: if you save only parts of a communication then Wireshark once again can't determine packet relationships on an application level. It needs to see certain "session setup" packets first to be able to determine what others are. If you save only parts of a conversation Wireshark cannot tell those packets apart anymore, and you'll get default descriptions like "Continuation or non-HTTP traffic".</p><p>OK, I hope I guessed correctly, because otherwise that was a lot of text for nothing :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '13, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26135" class="comments-container"><span id="26142"></span><div id="comment-26142" class="comment"><div id="post-26142-score" class="comment-score"></div><div class="comment-text"><p>"OK, I hope I guessed correctly, because otherwise that was a lot of text for nothing :-)" LOL! Classic!</p></div><div id="comment-26142-info" class="comment-info"><span class="comment-age">(17 Oct '13, 12:07)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="26143"></span><div id="comment-26143" class="comment"><div id="post-26143-score" class="comment-score"></div><div class="comment-text"><blockquote><p>OK, I hope I guessed correctly, because otherwise that was a lot of text for nothing :-)</p></blockquote><p>=:-))</p><p>O.K. let me guess too... Just with less text. ;-)</p><p>I <strong>guess</strong> that the OP used FTP to transfer the capture file and thereby used ASCII mode (instead of binary). By doing so, he modified the file (CRLF translation).</p><p>Regards<br />
Kurt</p></div><div id="comment-26143-info" class="comment-info"><span class="comment-age">(17 Oct '13, 12:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26158"></span><div id="comment-26158" class="comment"><div id="post-26158-score" class="comment-score"></div><div class="comment-text"><p>Yes, I tried to save all marked packets. I marked them one-by-one, because I didn't know another way. I expected to get back all marked packets, but it failed. I expected at least a warning, that it will not work. The solution was to specify a packet range, which contains all packets, which are of interest.</p></div><div id="comment-26158-info" class="comment-info"><span class="comment-age">(18 Oct '13, 01:12)</span> <span class="comment-user userinfo">pihentagy</span></div></div><span id="26159"></span><div id="comment-26159" class="comment"><div id="post-26159-score" class="comment-score"></div><div class="comment-text"><p>Makes sense - Wireshark needs the additional packets to be able to determine symptoms and communication flow. Things like that are not saved as meta data if you just extract the packets it concerns directly, so you lose that information if you do that.</p></div><div id="comment-26159-info" class="comment-info"><span class="comment-age">(18 Oct '13, 02:48)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-26135" class="comment-tools"></div><div class="clear"></div><div id="comment-26135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

