+++
type = "question"
title = "Huge traffic from 213.158.175.65"
description = '''I have found lately that I reach my internet use limit very fast while I&#x27;m sure we are not using that much that fast. So, I installed WireShark and left it on for a while with &quot;Statistics-&amp;gt; Endpoints&quot; open to track usage throughout all devices over the network.  I was expecting the traffic to be ...'''
date = "2017-01-21T16:52:00Z"
lastmod = "2017-01-23T20:43:00Z"
weight = 58939
keywords = [ "huge", "hetzner.de", "traffic" ]
aliases = [ "/questions/58939" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Huge traffic from 213.158.175.65](/questions/58939/huge-traffic-from-21315817565)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58939-score" class="post-score" title="current number of votes">0</div><span id="post-58939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have found lately that I reach my internet use limit very fast while I'm sure we are not using that much that fast. So, I installed WireShark and left it on for a while with "Statistics-&gt; Endpoints" open to track usage throughout all devices over the network. I was expecting the traffic to be huge from my Xbox but to my surprise I found that in the course of a couple hours there was more than 0.5 GB of data between my laptop and this IP: 213.158.175.65</p><p>I tracerouted this IP and found that it was hosted on hetzner.de That's all I could find. I have no idea what is happening. On my laptop I only have my browser open with a few tabs of facebook pages, my email, a university web page and a few google search results. There is no way these pages are consuming all that much. I have to note that during the two hours of sniffing I was not using my laptop at all. These pages were just open without any interaction from me.</p><p>The only connection I could make is that the university page I was opening is from Amsterdam university which might be hosted in the German servers.</p><p>Can someone shed some light on the weird behavior please? Cause overnight my network has consumed 18 GB of data with no reason at all. That's why I started the sniffing.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-huge" rel="tag" title="see questions tagged &#39;huge&#39;">huge</span> <span class="post-tag tag-link-hetzner.de" rel="tag" title="see questions tagged &#39;hetzner.de&#39;">hetzner.de</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '17, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/64a3be16659d3f069fe663de7ead7282?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ahmedn1&#39;s gravatar image" /><p><span>Ahmedn1</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ahmedn1 has no accepted answers">0%</span></p></div></div><div id="comments-container-58939" class="comments-container"><span id="58944"></span><div id="comment-58944" class="comment"><div id="post-58944-score" class="comment-score">3</div><div class="comment-text"><p>Are you sure about that host you tracerouted?</p></div><div id="comment-58944-info" class="comment-info"><span class="comment-age">(22 Jan '17, 04:27)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="58948"></span><div id="comment-58948" class="comment"><div id="post-58948-score" class="comment-score">1</div><div class="comment-text"><p>Hmmm. I have just checked that IP address from my end (Europe) and found a hostname in the domain tedata.net.</p><p>This matches the definition from the Hurricane Electric Looking Glass, which associates the IP address with the Egyptian provier te.net: <a href="http://bgp.he.net/AS8452#_prefixes">http://bgp.he.net/AS8452#_prefixes</a></p><p>Please remember that many e-mail clients constantly poll the mail servers and many web sites refresh their content with advertisements or news.</p></div><div id="comment-58948-info" class="comment-info"><span class="comment-age">(22 Jan '17, 06:56)</span> <span class="comment-user userinfo">packethunter</span></div></div><span id="58995"></span><div id="comment-58995" class="comment"><div id="post-58995-score" class="comment-score"></div><div class="comment-text"><p>Yes tedata is my ISP. But still I cannot explain the enormous bandwidth usage.</p></div><div id="comment-58995-info" class="comment-info"><span class="comment-age">(23 Jan '17, 20:43)</span> <span class="comment-user userinfo">Ahmedn1</span></div></div></div><div id="comment-tools-58939" class="comment-tools"></div><div class="clear"></div><div id="comment-58939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

