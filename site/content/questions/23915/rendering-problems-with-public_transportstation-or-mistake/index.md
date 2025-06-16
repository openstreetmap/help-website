+++
type = "question"
title = "Rendering problems with public_transport=station or mistake ?"
description = '''Hi all, I wanted to add more details to a train_station, I followed the new public_transport principles (https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport) but I think I did a mistake : platforms, and highway=foot with area=yes do not appear :  https://www.openstreetmap.org/?lat=4...'''
date = "2013-07-02T21:23:00Z"
lastmod = "2013-07-02T21:54:00Z"
weight = 23915
keywords = [ "rendering", "public_transport", "platform" ]
aliases = [ "/questions/23915" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering problems with public_transport=station or mistake ?](/questions/23915/rendering-problems-with-public_transportstation-or-mistake)

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
<span id="post-23915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23915-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I wanted to add more details to a train_station, I followed the new public_transport principles (<a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport">https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport</a>) but I think I did a mistake : platforms, and highway=foot with area=yes do not appear :</p>
<p><a href="https://www.openstreetmap.org/?lat=44.889148&amp;lon=6.633586&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=44.889148&amp;lon=6.633586&amp;zoom=18&amp;layers=M</a> and on the tiles view : <a href="http://tile.openstreetmap.fr/?zoom=18&amp;lat=44.88899&amp;lon=6.63228&amp;layers=B00000FFF">http://tile.openstreetmap.fr/?zoom=18&amp;lat=44.88899&amp;lon=6.63228&amp;layers=B00000FFF</a></p>
<p>Here is how I did : - The station area tagged with public_transport=station - The platform tagged with public_transport=platform - The approximative stop position tagged as stop_position - All of them in a relation (type=public_transport, public_transport=stop_area with the good roles (I think).</p>
<p>The platforms does not appear on the map. I saw it's not already supported on Mapnik due to migration to CartoCSS <a href="/questions/19349/rendering-of-public_transportplatform-on-mapnik">https://help.openstreetmap.org/questions/19349/rendering-of-public_transportplatform-on-mapnik</a> (didn't find anywhere if this is finsihed).</p>
<p>I tried to add highway=footway on platforms but it's not better.</p>
<p>Could you tell me if I made something wrong or if something is missing ?</p>
<p>Thanks,</p>
<p>Kévin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-public_transport" rel="tag" title="see questions tagged &#39;public_transport&#39;">public_transport</span> <span class="post-tag tag-link-platform" rel="tag" title="see questions tagged &#39;platform&#39;">platform</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '13, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/8c4c3fc6dd04450b7dc2c2e7077fa723?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="K_Peignot&#39;s gravatar image" />
<p><span>K_Peignot</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="K_Peignot has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '13, 21:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-23915" class="comments-container">
<span id="23916"></span>
<div id="comment-23916" class="comment">
<div id="post-23916-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The problem is that the pages in the wiki don't necessarily reflect actual usage by real mappers, or support by all the OSM editors, or (as described in the other help question that you link to) support by the renderers on the OSM website.</p>
<p>There's probably a website out there somewhere that supports the new schema; hopefully someone can add a pointer to it from here (and from the other help question).</p>
<p>Personally I think that it's a mistake to create a wiki page like the new public transport proposal with a "Rendering" section that doesn't contain in bold print ALMOST NOTHING SUPPORTS THIS SCHEMA YET.</p>
</div>
<div id="comment-23916-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 21:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23915-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

