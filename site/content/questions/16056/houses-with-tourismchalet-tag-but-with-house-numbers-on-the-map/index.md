+++
type = "question"
title = "Houses with tourism=chalet tag but with house numbers on the map"
description = '''Hi all. I&#x27;m drawing the ski resort guesthouses in Are, Sweden here is the link to the area: http://osm.org/go/0cYOx4hLV- . Theese houses look like this http://goo.gl/maps/CPMEM and are for rent during the ski season, so I believe tourism=chalet is a suitable tab for them. However, chalet are rendere...'''
date = "2012-09-14T08:34:00Z"
lastmod = "2012-09-14T11:16:00Z"
weight = 16056
keywords = [ "housenumbers", "chalet" ]
aliases = [ "/questions/16056" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Houses with tourism=chalet tag but with house numbers on the map](/questions/16056/houses-with-tourismchalet-tag-but-with-house-numbers-on-the-map)

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
<span id="post-16056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16056-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all. I'm drawing the ski resort guesthouses in Are, Sweden here is the link to the area: <a href="http://osm.org/go/0cYOx4hLV-">http://osm.org/go/0cYOx4hLV-</a> . Theese houses look like this <a href="http://goo.gl/maps/CPMEM">http://goo.gl/maps/CPMEM</a> and are for rent during the ski season, so I believe tourism=chalet is a suitable tab for them. However, chalet are rendered without house numbers on OSM, which makes it harder to navigate in the resort using the map. Is there a way to leave chalet tag and still have house numbers visible (like house in the first link)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-chalet" rel="tag" title="see questions tagged &#39;chalet&#39;">chalet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '12, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/056f96b4d8e9c512ff75efa314fe9003?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaga666&#39;s gravatar image" />
<p><span>gaga666</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaga666 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16056" class="comments-container">
&#10;</div>
<div id="comment-tools-16056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16056-form-container" class="comment-form-container">
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

<span id="16070"></span>

<div id="answer-container-16070" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16070-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-16070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should not remove a tag like "tourism=chalet" just because you have a rendering issue. What you can do is:</p>
<ol>
<li>submit a ticket on the <a href="https://trac.openstreetmap.org/">trac</a> system to change the rendering rules on Mapnik for your case. But this would fix it for one renderer, not for all. (BTW, your issue is maybe nonexistent on other maps)</li>
<li>or use an alternative tagging method. I tried to put the address on a node on the facade instead of the building itself <a href="https://www.openstreetmap.org/browse/way/180816909">here</a>. This is a very usual method of tagging addresses in major cities and is supported by applications like Nominatim. You can even improve it by moving the node to the entrance and add the "<a href="https://wiki.openstreetmap.org/wiki/Key:entrance">entrance</a>" tag. The result <a href="https://www.openstreetmap.org/?lat=63.399968&amp;lon=12.972376&amp;zoom=18&amp;layers=M">works fine with the highest zoom only</a> but is better than nothing.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '12, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '12, 11:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-16070" class="comments-container">
<span id="16078"></span>
<div id="comment-16078" class="comment">
<div id="post-16078-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, the method with additional node seems to work, but again only on maximum zoom level. I will probably create ticket in trac.</p>
</div>
<div id="comment-16078-info" class="comment-info">
<span class="comment-age">(14 Sep '12, 11:16)</span> <span class="comment-user userinfo">gaga666</span>
</div>
</div>
</div>
<div id="comment-tools-16070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16070-form-container" class="comment-form-container">
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

