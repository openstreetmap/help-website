+++
type = "question"
title = "wrong address on the map"
description = '''When entering the address: 10390 Santa Monica Blvd Los Angeles I obtain the wrong address on the map, using the API in our code OR using the openstreetmap website. Are you aware of any issue with addresses ? thanks.'''
date = "2017-12-18T23:24:00Z"
lastmod = "2017-12-20T15:33:00Z"
weight = 61268
keywords = [ "address" ]
aliases = [ "/questions/61268" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wrong address on the map](/questions/61268/wrong-address-on-the-map)

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
<span id="post-61268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61268-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When entering the address: 10390 Santa Monica Blvd Los Angeles I obtain the wrong address on the map, using the API in our code OR using the openstreetmap website. Are you aware of any issue with addresses ? thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '17, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/363b9704c1afad6e8bf23c6a7e26afdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MixR&#39;s gravatar image" />
<p><span>MixR</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MixR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61268" class="comments-container">
<span id="61270"></span>
<div id="comment-61270" class="comment">
<div id="post-61270-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot! which file should I edit to add manually the address ? thanks again !</p>
</div>
<div id="comment-61270-info" class="comment-info">
<span class="comment-age">(19 Dec '17, 00:52)</span> <span class="comment-user userinfo">MixR</span>
</div>
</div>
<span id="61271"></span>
<div id="comment-61271" class="comment">
<div id="post-61271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not a file as such, OSM is really just a big database.</p>
<p>Go to the <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> website, center the view over the location the address should be in, and then use the "edit" pull down to select an editor. As it sounds like this might be your first edit, I would suggest using the iD editor (you, may need to setup an OSM account first). The select the location the address should be and add some "tags". In this case the addr:housenumber and addr:street tags are the two you need. I don't use iD so am not sure how this operation works there but others tell me it is easy (I almost always us JOSM but others claim it has more of a learning curve).</p>
</div>
<div id="comment-61271-info" class="comment-info">
<span class="comment-age">(19 Dec '17, 01:06)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-61268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61268-form-container" class="comment-form-container">
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

<span id="61269"></span>

<div id="answer-container-61269" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61269-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many, actually most, addresses in the US are missing from OSM. That is definitely true in the Los Angeles area. So when you look up an address in OSM (I assume you are doing it on www.openstreetmap.org) the search instance (Nominatim) is most likely failing to find the address in OSM and then falling back to some other data set for an answer. Looking up the address you posted, it seems the fall back databases don't have that address either so it is simply pointing to an arbitrary location on the road.</p>
<p>The best way to deal with this is to fire up a OSM editor and add the address information that is missing to OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '17, 00:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-61269" class="comments-container">
<span id="61274"></span>
<div id="comment-61274" class="comment">
<div id="post-61274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought Nominatim did an import of all Tiger addresses in the US., see the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Installing_Tiger_housenumber_data_for_the_US">installation instructions</a>. So it is possible that Nominatim finds an address while it was not added to OSM. That does not mean however, that it is correctly located, nor that is is not useful to add addresses directly to OSM.</p>
</div>
<div id="comment-61274-info" class="comment-info">
<span class="comment-age">(19 Dec '17, 04:11)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="61275"></span>
<div id="comment-61275" class="comment">
<div id="post-61275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Generally Nominatim does try other sources if the address is not in OSM. But unless I did something wrong the address given in the question does not result in an exact address being found. I recall the "details" part of the Nominatim used to tell what database/source it found the address in but that does not seem to be the true anymore. <a href="https://nominatim.openstreetmap.org/details.php?place_id=170312410">https://nominatim.openstreetmap.org/details.php?place_id=170312410</a></p>
</div>
<div id="comment-61275-info" class="comment-info">
<span class="comment-age">(19 Dec '17, 05:14)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="61282"></span>
<div id="comment-61282" class="comment">
<div id="post-61282-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nitpick: When house numbers are missing in an area, I think it'd be more effective to survey the house numbers at street corners and add <a href="http://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation">address interpolation tags</a> than to tag just one random house in the middle of the street.</p>
</div>
<div id="comment-61282-info" class="comment-info">
<span class="comment-age">(20 Dec '17, 05:41)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="61287"></span>
<div id="comment-61287" class="comment">
<div id="post-61287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The TIGER address data is lets say "not particularly good", this is AFAIK on purpose (for privacy reasons etc).</p>
<p>In general there are only two ways to fix the issues: go out and survey the addresses (I've actually added address from mapillary in LA), or do an address data import (which is a lot of work and requires having suitably licensed data).</p>
</div>
<div id="comment-61287-info" class="comment-info">
<span class="comment-age">(20 Dec '17, 11:23)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="61295"></span>
<div id="comment-61295" class="comment">
<div id="post-61295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>With respect to address interpolation tags, its been a while since I checked but they don't seem to be well supported by a number of off line navigation apps. So I've been avoiding using them.</p>
<p>What I normally do when I find an address that I want to visit is missing from OSM is: Find the location through some other service (AddressToGPS on Android works for me) and go there. Once there I make a point of walking the block collecting addresses. If a commercial area I collect shop names, etc. too. I try to do the whole block for privacy reasons: If I only collect a house address for the one person I'm visiting it really stands out on the map. But if the addresses for the whole block are added to OSM the one place I actually visited does not stand out as much.</p>
<p>As long as you are visiting the area, collecting a dozen or so house numbers is not really more difficult than getting the addresses at either end of the block and using address interpolation tagging.</p>
</div>
<div id="comment-61295-info" class="comment-info">
<span class="comment-age">(20 Dec '17, 15:33)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-61269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61269-form-container" class="comment-form-container">
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

