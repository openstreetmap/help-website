+++
type = "question"
title = "Removing map data that might be wrong"
description = '''While mapping, I&#x27;ve recently come across roads that are very likely not to exist, at least when comparing their course to Bing (and other) satellite imagery. For example, I saw a road that, according to Bing, ended at a specific point. However, in OSM it was mapped as continuing after that point and...'''
date = "2014-10-03T09:04:00Z"
lastmod = "2014-10-03T22:52:00Z"
weight = 37250
keywords = [ "non-existent", "removal" ]
aliases = [ "/questions/37250" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Removing map data that might be wrong](/questions/37250/removing-map-data-that-might-be-wrong)

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
<span id="post-37250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While mapping, I've recently come across roads that are very likely not to exist, at least when comparing their course to Bing (and other) satellite imagery.</p>
<p>For example, I saw a road that, according to Bing, ended at a specific point. However, in OSM it was mapped as continuing after that point and it was even shown as being connected to another road. According to Bing and other satellite layers, it looked like there could not even be a path where this road was mapped.</p>
<p>So, is it suitable to remove the road where it probably doesn't exist, even though I'm not a local mapper and cannot verify this 100%?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-non-existent" rel="tag" title="see questions tagged &#39;non-existent&#39;">non-existent</span> <span class="post-tag tag-link-removal" rel="tag" title="see questions tagged &#39;removal&#39;">removal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '14, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/9b1b4e90f4146bc02ab2da5df7df202d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maturi0n&#39;s gravatar image" />
<p><span>Maturi0n</span><br />
<span class="score" title="44 reputation points">44</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maturi0n has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37250" class="comments-container">
<span id="37252"></span>
<div id="comment-37252" class="comment">
<div id="post-37252-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could add the osm url of the road to you query and someone local may recognise the area and may be able to verify. It could have been recently constructed though it seems as though you are viewing quite recent imagery to be so confident.</p>
</div>
<div id="comment-37252-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 09:19)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="37269"></span>
<div id="comment-37269" class="comment">
<div id="post-37269-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please do add a OSM URL to one of the places in question. If it is the United States, especially if it is in the rural western United States, it may be one of the old Tiger data imports which are notoriously inaccurate and definitely need to be cleaned up. If you are using JOSM there is a Tiger 2013 overlay which is generally better and can assist in cleaning up. But even that is far from perfect. It could be that ID and/or Potlatch have that image overlay too but I don't use them so I can't say.</p>
</div>
<div id="comment-37269-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 17:21)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="37275"></span>
<div id="comment-37275" class="comment">
<div id="post-37275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(re the "where in the world is this question about") I'd assumed from <a href="https://help.openstreetmap.org/questions/37191/rendering-a-russian-language-map">this previous question</a> that it's actually Ukraine and/or Moldova.</p>
</div>
<div id="comment-37275-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 18:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37279"></span>
<div id="comment-37279" class="comment">
<div id="post-37279-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As I am relatively new to OSM, I sadly don't know how to get a link to those roads. The concerned objects where "Krasnyj per." (Красный пер.) and a nameless road next to it, in the village of Parkany (Парканы) in Transnistria/Moldova. Sadly I don't know any local <em>mappers</em>, I know a person that lives there and that confirmed to me that both roads were mapped incorrectly. I have corrected this since then.</p>
<p>Whenever I stumble across such problems again, I will just leave a note, except for the rare cases where I have a local source. Thanks for the tips.</p>
</div>
<div id="comment-37279-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 21:33)</span> <span class="comment-user userinfo">Maturi0n</span>
</div>
</div>
<span id="37282"></span>
<div id="comment-37282" class="comment">
<div id="post-37282-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>to post a map link just zoom into the place in question then cut and paste this bit above the map, it this it? <a href="http://www.openstreetmap.org/way/83039146#map=16/46.8232/29.5197">http://www.openstreetmap.org/way/83039146#map=16/46.8232/29.5197</a></p>
</div>
<div id="comment-37282-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 22:52)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-37250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37250-form-container" class="comment-form-container">
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

<span id="37253"></span>

<div id="answer-container-37253" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37253-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-37253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The only way to be <em>really</em> sure is to go and have a look, so personally I'd add a <a href="http://wiki.openstreetmap.org/wiki/Note">note</a> suggesting that there might be a problem so that a local mapper can investigate. It's fairly easy to get OSM notes local to an area (so easy that even I <a href="https://github.com/SomeoneElseOSM/Notes01">wrote something</a> to do that), and local mappers can see and act on them.</p>
<p>As an alternative, perhaps find the main communications mechanisms that the local community uses (which might be <a href="http://wiki.openstreetmap.org/wiki/Contact">mailing lists, forum, IRC or something else</a>) and ask there? Someone may be able to give you an answer straight away.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '14, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-37253" class="comments-container">
<span id="37266"></span>
<div id="comment-37266" class="comment">
<div id="post-37266-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You could also mail the mapper that added it, remember that bing imagery can be several years out of date and a new road could have been constructed.</p>
</div>
<div id="comment-37266-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 16:03)</span> <span class="comment-user userinfo">trigpoint</span>
</div>
</div>
<span id="37274"></span>
<div id="comment-37274" class="comment">
<div id="post-37274-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Further note: the original question didn't indicate -where- he was editing. While the answers in general are correct, in the USA uncorrected TIGER data can be multiple kilometers off in some areas and can seem to be completly unrelated to aerial imagery.</p>
</div>
<div id="comment-37274-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 18:51)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37253-form-container" class="comment-form-container">
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

