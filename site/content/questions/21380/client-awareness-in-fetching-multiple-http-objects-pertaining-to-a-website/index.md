+++
type = "question"
title = "Client awareness in fetching multiple HTTP objects pertaining to a website"
description = '''Hi, I got a basic doubt regarding opening TCP connections to fetch multiple HTTP objects pertaining to a website. Here is an example: I clicked www.disney.com and captured port 53(DNS) packets associated to that site Sample queries included A www.disney.com A a.dilcdn.com A ajax.googleapis.com A cdn...'''
date = "2013-05-22T14:57:00Z"
lastmod = "2013-05-22T16:12:00Z"
weight = 21380
keywords = [ "objects", "http" ]
aliases = [ "/questions/21380" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Client awareness in fetching multiple HTTP objects pertaining to a website](/questions/21380/client-awareness-in-fetching-multiple-http-objects-pertaining-to-a-website)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21380-score" class="post-score" title="current number of votes">0</div><span id="post-21380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I got a basic doubt regarding opening TCP connections to fetch multiple HTTP objects pertaining to a website.</p><p>Here is an example:</p><p>I clicked www.disney.com and captured port 53(DNS) packets associated to that site</p><p>Sample queries included</p><p>A www.disney.com</p><p>A a.dilcdn.com</p><p>A ajax.googleapis.com</p><p>A cdnvideo.dolimg.com</p><p>etc..........</p><p>Here, on my browser i typed only www.disney.com but my doubt is who will inform to client that in order to get full page it needs to open connections to a.dilcdn.com ,ajax.............</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '13, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 May '13, 15:24</strong> </span></p></div></div><div id="comments-container-21380" class="comments-container"></div><div id="comment-tools-21380" class="comment-tools"></div><div class="clear"></div><div id="comment-21380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21382"></span>

<div id="answer-container-21382" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21382-score" class="post-score" title="current number of votes">3</div><span id="post-21382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A webpage consists of many objects, like images, javascript files, stylesheets etc. Most of the object are coming from the site itself or maybe another server in the same site (like: images.disney.com).</p><p>However, there can also be objects linked from other sites like the ones that you have found. Think of ad-banners, statistics (like google-analytics), or social media links (like facebook).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '13, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21382" class="comments-container"><span id="21383"></span><div id="comment-21383" class="comment"><div id="post-21383-score" class="comment-score"></div><div class="comment-text"><p>If it is from images.disney.com and assume that there is no load balancer in front of disney web farm so that it will result in different ip address compared to www.disney.com.In this case who will tell to client that "Hey! in order to get images from disney you need to go to images.disney.com"</p></div><div id="comment-21383-info" class="comment-info"><span class="comment-age">(22 May '13, 15:49)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="21384"></span><div id="comment-21384" class="comment"><div id="post-21384-score" class="comment-score"></div><div class="comment-text"><p>and in second case like analytics or Facebook who told to my client to open connections to ajax.googleapis.com or a.dilcdn.com.All i did was typing www.disney.com and waiting for objects to load but lot of things happened in back end.</p></div><div id="comment-21384-info" class="comment-info"><span class="comment-age">(22 May '13, 15:51)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="21385"></span><div id="comment-21385" class="comment"><div id="post-21385-score" class="comment-score">1</div><div class="comment-text"><p>There are links in the html file (or created by javascript code) pointing to the external objects. The browser needs to download the objects to be able to show the whole page. So in order to fetch the objects, it will need to do a dns lookup first :-)</p><p>(just like it does the dns lookup for www.disney.com)</p></div><div id="comment-21385-info" class="comment-info"><span class="comment-age">(22 May '13, 15:56)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-21382" class="comment-tools"></div><div class="clear"></div><div id="comment-21382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21386"></span>

<div id="answer-container-21386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21386-score" class="post-score" title="current number of votes">2</div><span id="post-21386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While Wireshark is pretty good at helping you work out how a browser works, you are probably better off using the debugging tools available for browsers. These probably allow better context for the various HTTP calls that are triggered.</p><p>Chrome has debugging tools under the Tools &gt; Developer Tools and then click the Network tab Firefox has the Firebug add on Internet Explorer has Tools &gt; Developer Tools (or press F12)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '13, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-21386" class="comments-container"></div><div id="comment-tools-21386" class="comment-tools"></div><div class="clear"></div><div id="comment-21386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

