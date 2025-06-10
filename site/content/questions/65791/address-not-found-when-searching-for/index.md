+++
type = "question"
title = "Address not found when searching for"
description = '''I&#x27;ve added the following address (see 47.31774, 8.42104 ) : addr:city = Arni (AG) addr:country = CH addr:housenumber = 1 addr:postcode = 8905 addr:street = Hüttenbach For some reason OSM can not find this address when searching for. What is wrong ?'''
date = "2018-09-06T20:19:00Z"
lastmod = "2018-09-06T20:30:00Z"
weight = 65791
keywords = [ "address" ]
aliases = [ "/questions/65791" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Address not found when searching for](/questions/65791/address-not-found-when-searching-for)

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
<span id="post-65791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65791-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've added the following address (see 47.31774, 8.42104 ) :</p>
<p>addr:city = Arni (AG) addr:country = CH addr:housenumber = 1 addr:postcode = 8905 addr:street = Hüttenbach</p>
<p>For some reason OSM can not find this address when searching for. What is wrong ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '18, 20:19</strong></p>
<img src="https://secure.gravatar.com/avatar/d59fb6ef25851761e8f54566d514bdb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Coordimaker&#39;s gravatar image" />
<p><span>Coordimaker</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Coordimaker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65791" class="comments-container">
&#10;</div>
<div id="comment-tools-65791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65791-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="65793"></span>

<div id="answer-container-65793" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65793-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A quick check here <a href="http://qa.poole.ch/ch-roads/AG/4061.html">http://qa.poole.ch/ch-roads/AG/4061.html</a> shows that the "whatever it is" Hüttenbach is missing. The search application on openstreetmap.org assumes that a street of place object of the name used in addr:street or addr:place exists. The "none" in the list is often used by municipalities to indicate a new development.</p>
<p>The simple solution is to either name the street in question or add a suitable place node.</p>
<p>Note we have access to address data for the whole of Switzerland here <a href="http://qa.poole.ch/addresses/ch/">http://qa.poole.ch/addresses/ch/</a> that may help in localizing the other missing objects.</p>
<p>Follow up: I quickly checked the GWR data and would suggest adding a place=neighbourhood node and using addr:place instead of addr:street for the addresses. Number 5 should get the addr:place too.</p>
<p>PS: waves direction Arni from about 10km away</p>
<p>PPS: lots of addresses in Arni are mapped with so called "associatedStreet" relations, this is no longer common practice (but shoud still work).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '18, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '18, 21:02</strong> </span></p>
</div>
</div>
<div id="comments-container-65793" class="comments-container">
&#10;</div>
<div id="comment-tools-65793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65793-form-container" class="comment-form-container">
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

