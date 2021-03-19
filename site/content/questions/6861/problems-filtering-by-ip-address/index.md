+++
type = "question"
title = "Problems filtering by IP Address"
description = '''I am using a mac running 10.6.8 and i am want to use wireshark to see the packet transmission between other devices on the network but i am having problems with this.  my current situation is that i am using ip.addr== &#x27;then my ip address&#x27;. If i put my own ip address in i can see all packets that are...'''
date = "2011-10-12T02:33:00Z"
lastmod = "2011-10-12T03:03:00Z"
weight = 6861
keywords = [ "wireless", "ethernet", "mac", "packets", "network" ]
aliases = [ "/questions/6861" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problems filtering by IP Address](/questions/6861/problems-filtering-by-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6861-score" class="post-score" title="current number of votes">0</div><span id="post-6861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using a mac running 10.6.8 and i am want to use wireshark to see the packet transmission between other devices on the network but i am having problems with this.</p><p>my current situation is that i am using ip.addr== 'then my ip address'. If i put my own ip address in i can see all packets that are either sent or received by my ip address. if i apply the same to another ip address, for example an ipad i cant see any tcp , http packets etc... i get a lot of mdns packets and these arent really useful to me. A similar thing happens if i try to put the ip address in of another mac on the same network. I see a lot of 'DropBox Discovery' packets again, not what im after.</p><p>is there something that im doing wrong, or not doing at all to mean that this isnt working?</p><p>I have also tried doing this on a wired ethernet connection and a wireless connection to the same network.</p><p>help please guys?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '11, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/2b5ceacc861c470afc612d72811198d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gengisnicky31&#39;s gravatar image" /><p><span>Gengisnicky31</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gengisnicky31 has no accepted answers">0%</span></p></div></div><div id="comments-container-6861" class="comments-container"></div><div id="comment-tools-6861" class="comment-tools"></div><div class="clear"></div><div id="comment-6861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6862"></span>

<div id="answer-container-6862" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6862-score" class="post-score" title="current number of votes">0</div><span id="post-6862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you're experiencing is the fact that today's networks are switched networks, not shared like when we were using hubs. Meaning: packets for each communication are only forwarded to the ports the nodes talking with each other are connected to, while all other devices do not get the packets (because they're not meant for them anyway). That is why you only see your own stuff, plus broadcast/multicast like MNDS (Multicast DNS).</p><p>This is a pretty common situation when doing network captures. If you want to get around it and capture packets for other devices you need to configure your switch to "copy" the packets to the port Wireshark is on. There are two drawbacks here: your switch needs to manageable and provide a mirror/monitor/SPAN feature, and you might not be able to communicate yourself anymore as soon as you configure your own port to be a monitor port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '11, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6862" class="comments-container"><span id="6863"></span><div id="comment-6863" class="comment"><div id="post-6863-score" class="comment-score"></div><div class="comment-text"><p>that explains a lot really. thanks for your reply. back to the drawing board i think... unless there are any other work arounds that are available/you know about?</p></div><div id="comment-6863-info" class="comment-info"><span class="comment-age">(12 Oct '11, 02:58)</span> <span class="comment-user userinfo">Gengisnicky31</span></div></div><span id="6865"></span><div id="comment-6865" class="comment"><div id="post-6865-score" class="comment-score"></div><div class="comment-text"><p>Well, you can also replace your switch with an old hub, but that will slow your network down. And if you're not on a stand alone switch but one integrated into a router you're more or less out of luck.</p><p>There are some not-so-nice techniques to get to packets of other nodes that require tools from the hacking community, for example Cain &amp; Abel. With those you can do ARP cache poisoning and reroute packets to your own node, but this is a) an unfriendly act, and b) not a wise thing to do in network analysis situations because it messes with the network behavior.</p></div><div id="comment-6865-info" class="comment-info"><span class="comment-age">(12 Oct '11, 03:03)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-6862" class="comment-tools"></div><div class="clear"></div><div id="comment-6862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

