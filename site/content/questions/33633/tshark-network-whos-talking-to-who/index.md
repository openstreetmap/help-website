+++
type = "question"
title = "tshark network whos talking to who"
description = '''I&#x27;m looking for a basic view of who is talking to who on the network. With TCPdump i was using tcpdump -q. It gave me IP to IP and what port. no more no less. Is that possible with tshark? '''
date = "2014-06-10T20:48:00Z"
lastmod = "2014-06-12T07:19:00Z"
weight = 33633
keywords = [ "tshark" ]
aliases = [ "/questions/33633" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark network whos talking to who](/questions/33633/tshark-network-whos-talking-to-who)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33633-score" class="post-score" title="current number of votes">0</div><span id="post-33633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for a basic view of who is talking to who on the network. With TCPdump i was using tcpdump -q. It gave me IP to IP and what port. no more no less. Is that possible with tshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '14, 20:48</strong></p><img src="https://secure.gravatar.com/avatar/ba4811c88d16330f68bbca30a49ce536?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dc2a&#39;s gravatar image" /><p><span>dc2a</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dc2a has no accepted answers">0%</span></p></div></div><div id="comments-container-33633" class="comments-container"></div><div id="comment-tools-33633" class="comment-tools"></div><div class="clear"></div><div id="comment-33633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33715"></span>

<div id="answer-container-33715" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33715-score" class="post-score" title="current number of votes">1</div><span id="post-33715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can change the column format of tshark to get a <strong>similar</strong> output (ports are not 'attached' to the IP addresses with a dot), with the following option: <strong>-o gui.column.format</strong></p><blockquote><p>tshark -nr test.pcap -o "gui.column.format:\"No.\",\"%m\",\"Time\",\"%t\",\"Source\",\"%s\",\"Source Port\",\"%S\",\"Destination\",\"%d\",\"Destination Port\",\"%D\""</p></blockquote><p>Result:</p><pre><code>  1 0.000000000 192.168.158.128 49722 80.67.16.195 443
  2 0.000143000 80.67.16.195 443 192.168.158.128 49722
  3 2.000479000 192.168.158.128 49724 80.67.16.195 443
  4 2.000485000 80.67.16.195 443 192.168.158.128 49724
  5 2.293298000 192.168.158.139 4620 162.159.242.165 80</code></pre><p>Another option would be the stats module of tshark</p><blockquote><p>tshark -nr test.pcap -q <strong>-z conv,tcp</strong></p></blockquote><p>Result (will show some details about the conversations as well)</p><pre><code>================================================================================
TCP Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |    Relative    |   Duration   |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |
192.168.158.139:4627 &lt;-&gt; 162.159.242.165:80       214    170550     111     24317     325    194867    85,416556000       260,7799
192.168.158.139:4645 &lt;-&gt; 173.230.134.104:80       226    246836      98     20368     324    267204   373,790640000       175,1330
192.168.158.139:4646 &lt;-&gt; 173.230.134.104:80       204    211482      91     19029     295    230511   374,597051000        98,9188</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '14, 07:23</strong> </span></p></div></div><div id="comments-container-33715" class="comments-container"></div><div id="comment-tools-33715" class="comment-tools"></div><div class="clear"></div><div id="comment-33715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33635"></span>

<div id="answer-container-33635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33635-score" class="post-score" title="current number of votes">0</div><span id="post-33635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might try the -Tfields option along with the -e options to define the columns you want to see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '14, 21:22</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-33635" class="comments-container"></div><div id="comment-tools-33635" class="comment-tools"></div><div class="clear"></div><div id="comment-33635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

