+++
type = "question"
title = "Embedded map in modal is fully zoomed out."
description = '''I&#x27;m not sure how to get the following behavior to work. I want to render an iframe embed in a modal and show the map when a modal comes up.  Whenever I try to add the iframe to a div that is display: none and then brought into view the map is all the way zoomed out. I have no problem if I use the sa...'''
date = "2014-03-02T23:33:00Z"
lastmod = "2015-03-18T12:29:00Z"
weight = 31195
keywords = [ "rendering", "embed" ]
aliases = [ "/questions/31195" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Embedded map in modal is fully zoomed out.](/questions/31195/embedded-map-in-modal-is-fully-zoomed-out)

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
<span id="post-31195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31195-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm not sure how to get the following behavior to work. I want to render an iframe embed in a modal and show the map when a modal comes up.</p>
<p>Whenever I try to add the iframe to a div that is <code>display: none</code> and then brought into view the map is all the way zoomed out. I have no problem if I use the same code and remove the <code>display: none</code> div from around it.</p>
<p>Any ideas on how to fix that?</p>
<p>Thanks for this awesome resource. Truly awesome.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-embed" rel="tag" title="see questions tagged &#39;embed&#39;">embed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '14, 23:33</strong></p>
<img src="https://secure.gravatar.com/avatar/cb1af1fae773efa19477c50827ebe998?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyro&#39;s gravatar image" />
<p><span>cyro</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31195" class="comments-container">
<span id="31197"></span>
<div id="comment-31197" class="comment">
<div id="post-31197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this related to OpenStreetMap in some way?</p>
<p>Most people render some tiles from somewhere using a Javascript library such as Leaflet or Openlayers - are you trying to do that, or something else?</p>
</div>
<div id="comment-31197-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 23:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="31198"></span>
<div id="comment-31198" class="comment">
<div id="post-31198-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Here is an example of what I'm trying to embed <code>&lt;iframe frameborder="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-122.480427%2C37.745703%2C-122.472427%2C37.753703&amp;amp;layer=mapnik&amp;amp;marker=37.749703%2C-122.476427" style="border: 1px solid black"&gt;&lt;/iframe&gt;</code></p>
</div>
<div id="comment-31198-info" class="comment-info">
<span class="comment-age">(03 Mar '14, 00:12)</span> <span class="comment-user userinfo">cyro</span>
</div>
</div>
<span id="33133"></span>
<div id="comment-33133" class="comment">
<div id="post-33133-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I experienced the same, trying to put the map in a Bootstrap 3 modal dialog. The map is loaded, but fully zoomed out.</p>
<p>Placed outside of the modal, the map is rendered correctly.</p>
</div>
<div id="comment-33133-info" class="comment-info">
<span class="comment-age">(13 May '14, 11:54)</span> <span class="comment-user userinfo">travellersam</span>
</div>
</div>
<span id="41775"></span>
<div id="comment-41775" class="comment">
<div id="post-41775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Subscribing to follow this thread. Same issue here. Manually reloading the frame fixes it (as does leaving the map visible to begin with). Neither of these is acceptable in my application. I've attempted to reload the iframe automatically from the parent on open but this isn't working out well. My next attempt will be to create the iframe visible but off the page and move it back onscreen when "opened". If that doesn't work I'll try a lightbox or something but that really messes up the UI I'm trying to achieve.</p>
</div>
<div id="comment-41775-info" class="comment-info">
<span class="comment-age">(18 Mar '15, 00:56)</span> <span class="comment-user userinfo">macgirvin</span>
</div>
</div>
</div>
<div id="comment-tools-31195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31195-form-container" class="comment-form-container">
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

<span id="41776"></span>

<div id="answer-container-41776" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41776-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My "next attempt" (see my previous comment) was successful. I created the iframe inside a div with position: absolute and left and top both set to -9999 but with display: block. So it's technically "visible" but you can't see it. A button click event switches it to relative and auto (putting it back into its normal place on the page - one can style this to simulate a modal bootstrap element). Works well. The tiling engine seems to have issues with being initialised inside a display: none container.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '15, 03:28</strong></p>
<img src="https://secure.gravatar.com/avatar/74685c9f342f159611317a68c2655218?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="macgirvin&#39;s gravatar image" />
<p><span>macgirvin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="macgirvin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41776" class="comments-container">
<span id="41779"></span>
<div id="comment-41779" class="comment">
<div id="post-41779-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, Leaflet (the map display library used by osm.org) doesn't like being initialised on a hidden div. See for example <a href="https://github.com/tombatossals/angular-leaflet-directive/issues/168">https://github.com/tombatossals/angular-leaflet-directive/issues/168</a> .</p>
</div>
<div id="comment-41779-info" class="comment-info">
<span class="comment-age">(18 Mar '15, 12:29)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41776" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41776-form-container" class="comment-form-container">
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

