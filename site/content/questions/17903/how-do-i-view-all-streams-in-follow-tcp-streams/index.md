+++
type = "question"
title = "How do I view all streams in &quot;Follow Tcp Streams?&quot;"
description = '''I have a number of tcpdump traces. With one I could view the entire set of HTTP streams in &quot;Follow TCP Stream&quot;, and the rest not. I&#x27;d like to be able to see all streams as in the first case and not sure how to make that happen. I tried various filters, e.g., &#x27;tcp.stream ge 0&#x27;, but it seems like wire...'''
date = "2013-01-23T11:12:00Z"
lastmod = "2014-02-25T09:55:00Z"
weight = 17903
keywords = [ "followtcpstream" ]
aliases = [ "/questions/17903" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I view all streams in "Follow Tcp Streams?"](/questions/17903/how-do-i-view-all-streams-in-follow-tcp-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17903-score" class="post-score" title="current number of votes">0</div><span id="post-17903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a number of tcpdump traces. With one I could view the entire set of HTTP streams in "Follow TCP Stream", and the rest not. I'd like to be able to see all streams as in the first case and not sure how to make that happen. I tried various filters, e.g., 'tcp.stream ge 0', but it seems like wireshark would automatically reset to its own filter - 'tcp.stream eq 0' Any suggestions would be appreciated.</p><p>Anh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-followtcpstream" rel="tag" title="see questions tagged &#39;followtcpstream&#39;">followtcpstream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '13, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/2aff8e0a396afc3dff59beb03ce6ad81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anguyen2548&#39;s gravatar image" /><p><span>anguyen2548</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anguyen2548 has no accepted answers">0%</span></p></div></div><div id="comments-container-17903" class="comments-container"></div><div id="comment-tools-17903" class="comment-tools"></div><div class="clear"></div><div id="comment-17903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17906"></span>

<div id="answer-container-17906" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17906-score" class="post-score" title="current number of votes">2</div><span id="post-17906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A little bit of tshark scripting is your friend:</p><pre><code>END=$(tshark -r http.pcap -T fields -e tcp.stream | sort -n | tail -1); for ((i=0;i&lt;=END;i++)); do echo $i; tshark -r http.pcap -qz follow,tcp,ascii,$i &gt; follow-stream-$i.txt;done</code></pre><p>... or expanded to a couple of lines for readability:</p><pre><code>END=$(tshark -r ../pcap/http.cap -T fields -e tcp.stream | sort -n | tail -1)
for ((i=0;i&lt;=END;i++))
do
    echo $i
    tshark -r ../pcap/http.cap -qz follow,tcp,ascii,$i &gt; follow-stream-$i.txt
done</code></pre><p>Which will result in one text file for each tcp stream :-)</p><p>(or you can use <a href="http://www.circlemud.org/jelson/software/tcpflow/">tcpflow</a> of course)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '13, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jan '13, 17:43</strong> </span></p></div></div><div id="comments-container-17906" class="comments-container"><span id="30185"></span><div id="comment-30185" class="comment"><div id="post-30185-score" class="comment-score"></div><div class="comment-text"><p>Great answers, and easily script-able. However I want to send all streams to ascii file (in tshark) because the above script takes a very long time to perform the action for the number of streams I am looking at (and reading from the FS each time for a new stream is most likely the bottleneck). Performing this action should be much faster in the tshark process, however I can't vouch for how easy it would be to code.</p><p>The -follow flag was probably not meant to see all streams... I'm betting it makes use of a tshark search function to find the datum it is looking to work with. Given I want to print streams to ascii and potentially create statistics on all streams, I imagine I should alter the code. Is there a good flag anyone might suggest as a starting point for my alterations?</p></div><div id="comment-30185-info" class="comment-info"><span class="comment-age">(25 Feb '14, 09:55)</span> <span class="comment-user userinfo">dbavedb</span></div></div></div><div id="comment-tools-17906" class="comment-tools"></div><div class="clear"></div><div id="comment-17906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17904"></span>

<div id="answer-container-17904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17904-score" class="post-score" title="current number of votes">0</div><span id="post-17904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't. Follow TCP Stream always shows only one TCP stream, so in order to see them all you have to look at them one after the other, you can't see them all at the same time.</p><p>The reason why you say that you could see an entire set of HTTP streams is probably because you've looked at a HTTP/1.1 connection that uses a persistent TCP stream to transfer multiple objects from a single server. As soon as you do non-persistent TCP streaming (for example, in HTTP/1.0 or if the server denies persistence), or if multiple TCP connections to various servers are needed you'll get one TCP stream per HTTP object - and then you can't see them all in one "Follow TCP Stream"-window.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '13, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jan '13, 11:54</strong> </span></p></div></div><div id="comments-container-17904" class="comments-container"></div><div id="comment-tools-17904" class="comment-tools"></div><div class="clear"></div><div id="comment-17904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

