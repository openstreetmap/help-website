+++
type = "question"
title = "Building customized filters"
description = '''Hi,  How can I create/customize display-filters depending on coming packets in away that is (automatically) applied every time I start capturing filters. Lets say I want to filter all packets that are coming to the network from IP: 216.27.61.137 Thank you in advance, '''
date = "2013-10-28T14:11:00Z"
lastmod = "2013-11-04T15:52:00Z"
weight = 26488
keywords = [ "osx", "api", "display-filter" ]
aliases = [ "/questions/26488" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Building customized filters](/questions/26488/building-customized-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26488-score" class="post-score" title="current number of votes">0</div><span id="post-26488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, How can I create/customize display-filters depending on coming packets in away that is (automatically) applied every time I start capturing filters. Lets say I want to filter all packets that are coming to the network from IP: 216.27.61.137 Thank you in advance,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '13, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/704692ae10f63a2d03a4f0243de8ed4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OhudSaud&#39;s gravatar image" /><p><span>OhudSaud</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OhudSaud has no accepted answers">0%</span></p></div></div><div id="comments-container-26488" class="comments-container"><span id="26494"></span><div id="comment-26494" class="comment"><div id="post-26494-score" class="comment-score"></div><div class="comment-text"><p>Could you elaborate a bit, especially with your example, because I don't understand what it is you're asking for exactly.</p><p>With your example, you could use a capture filter of <code>host 216.27.61.137</code> to capture those packets of interest to you. But then you want some display filter to be automatically applied whenever you use that capture filter, is that right? If so, which display filter should be automatically applied in that case?</p></div><div id="comment-26494-info" class="comment-info"><span class="comment-age">(28 Oct '13, 18:43)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="26666"></span><div id="comment-26666" class="comment"><div id="post-26666-score" class="comment-score"></div><div class="comment-text"><p>I wanna use some kind of API where I can build filers that can color this IP without need to specify it. Like once the capturing started, Wireshark can color packets even though IPs are new to the network, if they some condition is true. Is there any possibility to do that? Thank you Chris,</p></div><div id="comment-26666-info" class="comment-info"><span class="comment-age">(04 Nov '13, 13:29)</span> <span class="comment-user userinfo">OhudSaud</span></div></div><span id="26669"></span><div id="comment-26669" class="comment"><div id="post-26669-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, but it is still unclear (at least for me) what you are trying to do.</p><p>Do you want to tell a running instance of Wireshark (via some API) to colorize traffic of a certain IP address, like:</p><ul><li>Now colorize IP:216.27.61.137 with color RED</li><li>Now colorize IP:1.2.3.4 with color GREEN</li></ul><p>If so: Why do you want to do that? What do you hope to see in the GUI that scrolls the incoming traffic?</p><p>If no: Please be more precise in the description of what you are trying to do.</p><blockquote><p>Wireshark can color packets <strong>even though IPs are new to the network</strong></p></blockquote><p>What does that mean? 'New to the network'?</p></div><div id="comment-26669-info" class="comment-info"><span class="comment-age">(04 Nov '13, 15:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26488" class="comment-tools"></div><div class="clear"></div><div id="comment-26488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

