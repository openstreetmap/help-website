+++
type = "question"
title = "Confused about discrepancy between Wireshark log and router log"
description = '''Greetings all - hopefully you can help me out because I really don&#x27;t know much about networking but have something on my network that is eating up a bunch of bandwidth on my ISP (showed up about a month ago - I started getting warnings from my ISP). I think Wireshark can help me figure out what&#x27;s ea...'''
date = "2015-06-19T18:13:00Z"
lastmod = "2015-06-21T10:54:00Z"
weight = 43393
keywords = [ "usage", "internet" ]
aliases = [ "/questions/43393" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Confused about discrepancy between Wireshark log and router log](/questions/43393/confused-about-discrepancy-between-wireshark-log-and-router-log)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43393-score" class="post-score" title="current number of votes">0</div><span id="post-43393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings all - hopefully you can help me out because I really don't know much about networking but have something on my network that is eating up a bunch of bandwidth on my ISP (showed up about a month ago - I started getting warnings from my ISP). I think Wireshark can help me figure out what's eating up all the bandwidth but I'm not quite sure how.</p><p>I'm just looking for info on how to sort internet usage by IP address. I found this thread:</p><p><a href="https://ask.wireshark.org/questions/9900/need-to-find-which-ip-address-is-taking-most-bandwith-usage-in-my-network?">https://ask.wireshark.org/questions/9900/need-to-find-which-ip-address-is-taking-most-bandwith-usage-in-my-network?</a></p><p>that seems to answer the question on how to do that. However, when I run the "Endpoints" summary sorted by IPv4 and look at the "Bytes" column I see 10x - 100x the usage that's reported by my router during the same time interval. The totals on my router are consistent with what I'm seeing from my ISP so that tells me I don't really know what I'm measuring with Wireshark...!</p><p>Now, I believe that what shows up under the "IPv4 Endpoint" summary could very well contain a lot of traffic that has no effect on my ISP usage. I have several computers on my network, and they use IPv4 to talk, right? So if they're just talking to each other then, indeed, that would not show up on my ISP usage. Do I understand that correctly?</p><p>If so, how do I use Wireshark to extract only the traffic that counts against my Internet traffic (sorted by IP address, of course)?</p><p>Alternatively, is there an easier way to accomplish this task?</p><p>I realize this is probably Networking 101, so thanks in advance!</p><p>rgames</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-internet" rel="tag" title="see questions tagged &#39;internet&#39;">internet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '15, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/d3d08f80f172fbfe6b3e5b3933b17b4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgames&#39;s gravatar image" /><p><span>rgames</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgames has no accepted answers">0%</span></p></div></div><div id="comments-container-43393" class="comments-container"></div><div id="comment-tools-43393" class="comment-tools"></div><div class="clear"></div><div id="comment-43393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43395"></span>

<div id="answer-container-43395" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43395-score" class="post-score" title="current number of votes">0</div><span id="post-43395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, as the other thread explains you need to take a trace on the router to get the statistics of all your internet traffic and then apply the Statistics -&gt; Endpoint method.<br />
If you have a trace taken on your device you can only measure your own internet usage by filtering on IP packets to and from your router's MAC address. The filter would be<br />
</p><p>eth.addr==xx:xx:xx:xx:xx:xx: and (ip or ipv6)</p><hr /><p>Update:</p><p>Ok, understood: You see more traffic than is being sent/received to/from your ISP. In this case it must be local traffic which you want excluded from the calculation ...</p><p>A display/capture filter that only<br />
"captures/displays packets where at least one IP address in the conversation is non-local"<br />
is what you need I suppose... Try the following filter and look at the Statistics -&gt; Endpoints and see if it serves your purpose<br />
<code>!ip.addr==192.168.1.0/24</code></p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '15, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '15, 12:35</strong> </span></p></div></div><div id="comments-container-43395" class="comments-container"><span id="43406"></span><div id="comment-43406" class="comment"><div id="post-43406-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply!</p><p>I'm still confused, though, because I think I'm getting all the traffic - in fact, as I described, Wireshark is showing a lot MORE traffic than is reported by my router or ISP. I understand how to sort by IP address and have done so - again, when I sort by IP I get a lot MORE traffic than reported by my router or ISP.</p><p>Maybe this example will help explain where I'm stuck: if I run a capture for 10 minutes and monitor my Internet traffic on my router I get, say, 10 MB of Internet traffic. But if I look at just one IP address in the Wireshark output, say 192.168.1.2, it shows 100 MB of traffic on my network over the same time period. That tells me that Wireshark is measuring a lot of traffic that has nothing to do with my ISP usage.</p><p>So, I can see all the devices on my network and the traffic associated with them (I think...!). Further, I know how to sort the output to show the traffic for each.</p><p>I need to figure out how to show only the traffic that is counted against my ISP usage.<br />
</p><p>Thanks again,</p><p>rgames</p></div><div id="comment-43406-info" class="comment-info"><span class="comment-age">(21 Jun '15, 09:55)</span> <span class="comment-user userinfo">rgames</span></div></div><span id="43410"></span><div id="comment-43410" class="comment"><div id="post-43410-score" class="comment-score"></div><div class="comment-text"><p><span>@rgames</span>: I converted your answer to a comment, as that's how this Q&amp;A site works. Please read the FAQ.</p></div><div id="comment-43410-info" class="comment-info"><span class="comment-age">(21 Jun '15, 10:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-43395" class="comment-tools"></div><div class="clear"></div><div id="comment-43395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

