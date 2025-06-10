+++
type = "question"
title = "Map on our website doesn&#x27;t work on iPhone"
description = '''Hi Guys, Our maps don&#x27;t work on iphone, any iphone, they work on iPads.  Any idea why this is? Here&#x27;s an example: https://www.colmcille.org/en/map-marker-route/gleann-cholm-cille/'''
date = "2021-11-23T12:42:00Z"
lastmod = "2021-11-23T15:27:00Z"
weight = 82658
keywords = [ "website", "leaflet", "iphone" ]
aliases = [ "/questions/82658" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Map on our website doesn't work on iPhone](/questions/82658/map-on-our-website-doesnt-work-on-iphone)

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
<span id="post-82658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82658-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys,</p>
<p>Our maps don't work on iphone, any iphone, they work on iPads.</p>
<p>Any idea why this is?</p>
<p>Here's an example: <a href="https://www.colmcille.org/en/map-marker-route/gleann-cholm-cille/">https://www.colmcille.org/en/map-marker-route/gleann-cholm-cille/</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '21, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/e14c263b574077a1560a94637d73702c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidHenry&#39;s gravatar image" />
<p><span>DavidHenry</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidHenry has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '21, 14:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-82658" class="comments-container">
&#10;</div>
<div id="comment-tools-82658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82658-form-container" class="comment-form-container">
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

<span id="82660"></span>

<div id="answer-container-82660" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82660-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-82660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First rule of computer problem-solving: don't use the phrase "it doesn't work". It's not helpful. Instead: What do you expect to happen? What happens instead? Can you give screenshots?</p>
<p>Here's what I'd do to debug:</p>
<ul>
<li>Connect an iPhone to a Mac. Open Safari on the Mac. Make sure the Develop menu is enabled.</li>
<li>From the Develop menu, select "iPhone" (or whatever the phone is called) and the title of your page in the subsequent menu.</li>
<li>The developer console will open for that window on your phone.</li>
<li>Press Command-Option-R to reload the page.</li>
<li>Make sure "Console" and "All" are selected, so you can see any errors that your page is outputting.</li>
</ul>
<p>When I do this, I see the following errors:</p>
<ul>
<li>jQuery.Deferred exception: undefined is not an object (evaluating 'screenfull.raw.fullscreenchange')</li>
<li>_createButton — Control.FullScreen.js:80</li>
<li>TypeError: undefined is not an object (evaluating 'screenfull.raw.fullscreenchange')</li>
</ul>
<p>So you've got a problem with the code in Control.FullScreen.js, i.e. the Leaflet full-screen control that you're using. There appear to be some reported issues with it on the iPhone: see <a href="https://github.com/Leaflet/Leaflet.fullscreen/issues">https://github.com/Leaflet/Leaflet.fullscreen/issues</a> . Try removing this plugin and trying again.</p>
<p>This is basic JavaScript debugging, not specific to OSM. If your developer doesn't know how to do this you should possibly get a new developer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '21, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '21, 14:53</strong> </span></p>
</div>
</div>
<div id="comments-container-82660" class="comments-container">
<span id="82661"></span>
<div id="comment-82661" class="comment">
<div id="post-82661-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Richard, this got us started on the fix :)</p>
<p>Just to confirm, the issue was on iPhone devices the map showed as grey so the tiles were not loading. Fixing an error in our custom leaflet.js fixed it.</p>
</div>
<div id="comment-82661-info" class="comment-info">
<span class="comment-age">(23 Nov '21, 15:27)</span> <span class="comment-user userinfo">DavidHenry</span>
</div>
</div>
</div>
<div id="comment-tools-82660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82660-form-container" class="comment-form-container">
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

