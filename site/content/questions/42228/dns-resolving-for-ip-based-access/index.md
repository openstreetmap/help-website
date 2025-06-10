+++
type = "question"
title = "DNS resolving for IP based access"
description = '''At our customer we are making an internet connection possible for clients only for the public IP adressess of Openstreetmap.org. The access list is configured in the switch and therefore we need all the public IP adresses which can be resolved by the DNS for the following DNS names:  a.tile.openstre...'''
date = "2015-04-09T10:33:00Z"
lastmod = "2015-04-09T12:29:00Z"
weight = 42228
keywords = [ "tiles", "dns", "tileserver" ]
aliases = [ "/questions/42228" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DNS resolving for IP based access](/questions/42228/dns-resolving-for-ip-based-access)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42228-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>At our customer we are making an internet connection possible for clients only for the public IP adressess of Openstreetmap.org.</p>
<p>The access list is configured in the switch and therefore we need all the public IP adresses which can be resolved by the DNS for the following DNS names:</p>
<ul>
<li>a.tile.openstreetmap.org</li>
<li>b.tile.openstreetmap.org</li>
<li>c.tile.openstreetmap.org</li>
</ul>
<p>At the wiki I found multiple public addresses but a few public adresses we found cannot be found in the WIKI.</p>
<p>Here are all the addresses we resolved to date:</p>
<ul>
<li>78.47.89.101</li>
<li>78.47.106.69</li>
<li>78.47.126.11</li>
<li>78.47.233.251</li>
</ul>
<p>We would like to get the full list of public IP adresses that can be resolved for the above DNS names.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '15, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/78fce3b84cb2ec7be40b6480b3d02620?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaartenBrok&#39;s gravatar image" />
<p><span>MaartenBrok</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaartenBrok has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Apr '15, 12:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42228" class="comments-container">
&#10;</div>
<div id="comment-tools-42228" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42228-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42231"></span>

<div id="answer-container-42231" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42231-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap uses DNS resolving based on geo location, so the IP numbers you get will be dependent on the network you are calling from, on what is assumed to be your location, and on the current configuration of the OSM tile CDN. Additional IP numbers can show up at any time, when additional or different tile proxies are configured for your region. Configuring the list of IP numbers in a switch sounds like asking for trouble to me!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '15, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42231" class="comments-container">
&#10;</div>
<div id="comment-tools-42231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42231-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42233"></span>

<div id="answer-container-42233" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42233-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe setting up a local <span>caching proxy</span> would be an alternative option for you: no IP address problems and (if your users often view the same areas) possibly faster load times, less load on your Internet connection, less load on the donation-driven OSM.org tile servers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '15, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Apr '15, 13:06</strong> </span></p>
</div>
</div>
<div id="comments-container-42233" class="comments-container">
&#10;</div>
<div id="comment-tools-42233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42233-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

