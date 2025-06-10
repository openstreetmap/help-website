+++
type = "question"
title = "Extract block number from address located in Bahrain Country"
description = '''Bahrain has a block number for a destination, I can get it on Google Maps API but, I need to use OSM for another usage, so, my question is this possible or not? I want to get the block number of an address located in Bahrain. First of all, let me show you what block numbers are. Bahrain is divided i...'''
date = "2020-04-26T22:43:00Z"
lastmod = "2020-04-27T14:02:00Z"
weight = 74384
keywords = [ "bahrain", "android", "osm" ]
aliases = [ "/questions/74384" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extract block number from address located in Bahrain Country](/questions/74384/extract-block-number-from-address-located-in-bahrain-country)

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
<span id="post-74384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74384-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Bahrain has a block number for a destination, I can get it on Google Maps API but, I need to use OSM for another usage, so, my question is this possible or not?</p>
<p>I want to get the block number of an address located in Bahrain.</p>
<p>First of all, let me show you what block numbers are. Bahrain is divided into areas and each area has a block number like in the photo below:</p>
<p><a href="https://i.stack.imgur.com/bEkWV.png"><img src="https://i.stack.imgur.com/bEkWV.png" alt="enter image description here" /></a></p>
<p>So, I hope the block number becomes clear to you now.</p>
<p>I've implemented a basic app to get the location and some of its info like this:</p>
<p><a href="https://i.stack.imgur.com/lKJX2.png"><img src="https://i.stack.imgur.com/lKJX2.png" alt="enter image description here" /></a></p>
<p>This address is located in <code>BLOCK 326</code> but I don't have any idea about how to get the correct block number.</p>
<p>This feature is already built into the <code>Uber</code> and <code>trycarriage</code> apps.</p>
<p>I'm using the OSM API to get my data.</p>
<p>Any good ideas about how this can be done?</p>
<p>I know how to do that in Google maps but how do I achieve this in OSM? Are these values available on the OSM map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bahrain" rel="tag" title="see questions tagged &#39;bahrain&#39;">bahrain</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '20, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/24cc1be0ca7b8bc2e333f87b79457d46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Moustafa%20Mahmoud&#39;s gravatar image" />
<p><span>Moustafa Mah...</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Moustafa Mahmoud has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-74384" class="comments-container">
&#10;</div>
<div id="comment-tools-74384" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74384-form-container" class="comment-form-container">
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

<span id="74415"></span>

<div id="answer-container-74415" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74415-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>Your block numbers look a bit like postal codes, you could use the dedicated tags IMHO. Several tagging schemes are supported :</p>
<ul>
<li>Draw an area with <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dpostal_code">boundary=postal_code</a></li>
<li>Put the <a href="https://wiki.openstreetmap.org/wiki/Key:postal_code">postal_code</a> tag on streets.</li>
<li>Put the <a href="https://wiki.openstreetmap.org/wiki/Key:addr">addr:postcode</a> tag on individual addresses, via dedicated nodes or on the buildings</li>
</ul>
<p>The advantage is that postal code are supported in most OSM-related software.</p>
<p>On the other hand, you might think that the block numbers have not much to do with postal addresses.</p>
<p>In this case, <a href="https://wiki.openstreetmap.org/wiki/Tag:place%3Dsuburb">place=suburb</a>, or the smaller <a href="https://wiki.openstreetmap.org/wiki/Tag:place%3Dneighbourhood">place=neighbourhood</a> might suit you better.</p>
<p>As for other tagging questions, the <a href="https://lists.openstreetmap.org/listinfo/tagging">tagging mailing-list</a> would be the right place to discuss new tag usage.</p>
<p>Once you decide on a tag, you'll need to actually find the data to add it to OSM. You can't copy it from Google (or others) because their license won't allow it. You might find an (government) official source, you usually need to ask for specific permission. Then you'll need to follow the <a href="https://wiki.openstreetmap.org/wiki/Import">import process</a>.</p>
<p>Or you can just start slowly, adding the blocks you know from personal knowledge. This is harder if you tag the blocks as areas, as it's hard to guess to boundaries from personal knowledge of few addresses.</p>
<p>Hope this helps. Please ask if you need help on specific part of the process.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '20, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</img>
</div>
</div>
<div id="comments-container-74415" class="comments-container">
&#10;</div>
<div id="comment-tools-74415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74415-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74416"></span>

<div id="answer-container-74416" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74416-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, sorry I reread your question, you're not asking how to add the data, but if it's already there.</p>
<p>Short answer is no.</p>
<p>There is one <a href="https://www.openstreetmap.org/node/1142037185">node</a> with an "addr:block" tag, which makes sense and is actually <a href="https://wiki.openstreetmap.org/wiki/Key:addr#Detailed_subkeys">documented</a> (even if it's to say "does not seem to be widely accepted nor interpreted").</p>
<p>A <a href="https://www.openstreetmap.org/way/485936811">few</a> put it in the street name ("addr:street").</p>
<p>At least <a href="https://www.openstreetmap.org/node/4381195790">one</a> put it in "addr:housenumber".</p>
<p>Here is a query to find all these examples : <a href="https://overpass-turbo.eu/s/Tme">https://overpass-turbo.eu/s/Tme</a></p>
<p>So it seems there is a need to establish a convention, and start adding data. :-)</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '20, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74416" class="comments-container">
&#10;</div>
<div id="comment-tools-74416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74416-form-container" class="comment-form-container">
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

