+++
type = "question"
title = "How do I clear the image cache in JOSM"
description = '''Is there a simple method to clear the imagery cache in JOSM? When I go to download an area near where I&#x27;m mapping, boundaries of the Kodiak NWR I replaced two weeks ago still show unless I zoom in very close. Presumably, the data is stored somewhere and takes a while (a long while?) to update on JOS...'''
date = "2018-11-30T06:01:00Z"
lastmod = "2018-12-02T10:18:00Z"
weight = 66995
keywords = [ "josm", "clear", "image_cache" ]
aliases = [ "/questions/66995" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I clear the image cache in JOSM](/questions/66995/how-do-i-clear-the-image-cache-in-josm)

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
<span id="post-66995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66995-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a simple method to clear the imagery cache in JOSM?</p>
<p>When I go to download an area near where I'm mapping, boundaries of the Kodiak NWR I replaced two weeks ago still show unless I zoom in very close. Presumably, the data is stored somewhere and takes a while (a long while?) to update on JOSM's internal slippy map.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-clear" rel="tag" title="see questions tagged &#39;clear&#39;">clear</span> <span class="post-tag tag-link-image_cache" rel="tag" title="see questions tagged &#39;image_cache&#39;">image_cache</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '18, 06:01</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '18, 06:02</strong> </span></p>
</div>
</div>
<div id="comments-container-66995" class="comments-container">
&#10;</div>
<div id="comment-tools-66995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66995-form-container" class="comment-form-container">
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

<span id="66998"></span>

<div id="answer-container-66998" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66998-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Go to JOSM's imagery preferences, go to the <a href="https://josm.openstreetmap.de/wiki/Help/Preferences/Imagery#Cachecontents">"Cache contents"</a> tab, and use the "Clear" button in the relevant line.</p>
<p>The tiles for the JOSM download dialog window can be deleted by using the "delete" button in <a href="https://josm.openstreetmap.de/ticket/17054">the "<em>Mapnik</em>"</a> line (needs restarting afterwards).<br />
Technical details (and the hard way of deletion): The tiles are saved in <code>~/.cache/JOSM/tiles</code>. For me exactly in the files <code>TMS_BLOCK_v2.data</code> and <code>TMS_BLOCK_v2.key</code> (stored with the key "Mapnik" if I see correctly). Deletion of the whole directory or just both files results in JOSM downloading the tiles when opening the download dialog.</p>
<p>Tested with version 14460 on Linux. For cache paths of other operating systems see <a href="https://josm.openstreetmap.de/wiki/Help/Preferences#JOSMpreferencedatacachedirectories">JOSM help</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '18, 06:55</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '18, 10:33</strong> </span></p>
</div>
</div>
<div id="comments-container-66998" class="comments-container">
<span id="67004"></span>
<div id="comment-67004" class="comment">
<div id="post-67004-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I cleared all imagery caches and restarted JOSM but that did not do it. By the way, the caches are named for the imagery source. Hence, there are Clear buttons for DigitalGlobe-Premium, DigitalGlobe-standard, USGS Topo, etc.</p>
<p>It's the slippy map that displays the outdated information, not the display inside the editor window. I guess we need to find a way to clear that.</p>
</div>
<div id="comment-67004-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 13:07)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="67018"></span>
<div id="comment-67018" class="comment">
<div id="post-67018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5016/alaskadave"></a><a href="https://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a>, oh, I interpreted "Kodiak NWR" to be a imagery name, sorry. Have updated my answer.</p>
<p>So, which imagery are you downloading? Or do you mean the imagery in the JOSM Download area selection dialog? This one is apparently independent from the "OpenStreetMap Carto (Standard)" background imagery layer. Whyever... I have updated my answer. Does it work for you?</p>
</div>
<div id="comment-67018-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 21:10)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67020"></span>
<div id="comment-67020" class="comment">
<div id="post-67020-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Let me explain. I added the Kodiak National Wildlife Refuge to OSM piece by piece (it's a huge refuge) over a period of two or three weeks. The original small piece still shows up at low zoom in the JOSM Download area window even though the refuge is now complete. I know it takes a while for the rendering on the slippy map to catch up with reality but two weeks seemed an awfully long time. I was looking for a way to speed that process up. I thought perhaps there was a way to force it by deleting any cached imagery.</p>
<p>I deleted the Mapnik cache along with the other image caches and restarted during my first try at this. It had no effect. I might try deleting the images in the cache but this isn't a big deal. Maybe I'll just have to be patient.</p>
<p>Dave</p>
<p>(I'm also running the latest JOSM - v14460 on Windows 10)</p>
</div>
<div id="comment-67020-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 01:49)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="67022"></span>
<div id="comment-67022" class="comment">
<div id="post-67022-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a>: hmm, well, is the Kodiak NWR shown in your updated version in your browser? If not then probably the rendering is just not yet updated. Note that lower zoom levels will take longer to update.</p>
<p>For a better understanding you may want to start JOSM from command line, then you see JOSM logging network requests (tile downloads) in the command line window.</p>
</div>
<div id="comment-67022-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 09:06)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67023"></span>
<div id="comment-67023" class="comment">
<div id="post-67023-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No problem. I'll just wait. It took several weeks for the Download window to show a state park I added.</p>
<p>Thanks for your help.</p>
</div>
<div id="comment-67023-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 10:18)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="67026"></span>
<div id="comment-67026" class="comment not_top_scorer">
<div id="post-67026-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At the moment, rendering at z13 and higher shouldn't be delayed except when the style has been refreshed. It seems here something got stuck.</p>
<p>You can ask the server to generate a new tile, by visiting, for example, <a href="https://a.tile.openstreetmap.org/9/36/156.png/dirty">https://a.tile.openstreetmap.org/9/36/156.png/dirty</a> which is just a nearby tile url with <code>/dirty</code> appended. Doing that for several zoom levels has things looking a bit better, but there are still some zooms that aren't updated.</p>
</div>
<div id="comment-67026-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 13:35)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="67036"></span>
<div id="comment-67036" class="comment not_top_scorer">
<div id="post-67036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>,</p>
<p>Thank you. I might try that in the future but I think I'll just wait it out. I've moved on to other projects now.</p>
</div>
<div id="comment-67036-info" class="comment-info">
<span class="comment-age">(02 Dec '18, 10:18)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-66998" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-66998-form-container" class="comment-form-container">
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

