+++
type = "question"
title = "License for a map of the world produced using OSM"
description = '''I’ve read the help pages about the Open Database License on the OSM wiki several times, but I’m still not sure I understand it. Assume I want to produce a map of the world like that using OSM data. I will need to extract the relevant data (coastlines, names and boundaries of countries) from OSM, sim...'''
date = "2013-07-23T23:03:00Z"
lastmod = "2013-07-24T08:10:00Z"
weight = 24501
keywords = [ "legal", "license" ]
aliases = [ "/questions/24501" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [License for a map of the world produced using OSM](/questions/24501/license-for-a-map-of-the-world-produced-using-osm)

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
<span id="post-24501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24501-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I’ve read the help pages about the Open Database License on the OSM wiki several times, but I’m still not sure I understand it.</p>
<p>Assume I want to produce a map of the world like <a href="http://commons.wikimedia.org/wiki/File:BlankMap-World6.svg">that</a> using OSM data. I will need to extract the relevant data (coastlines, names and boundaries of countries) from OSM, simplify the polygons to have something not too big and then generate the SVG.</p>
<p><strong>What are the legal requirements for the final SVG map? Can I release it into in the public domain or do I need to release it under the ODbL?</strong></p>
<p>My current understanding is that I can release the SVG into the public domain (it’s the Produced Work) but that the data used just before generating the SVG (i.e. the simplified boundaries) has to be released under the ODbL (it’s the Derivative Database). That would a bit strange, because once the SVG is in the public domain it’s easy to lose track of the database used to generate it (so it’s basically useless to have it under the ODbL), so maybe I misunderstood it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-legal" rel="tag" title="see questions tagged &#39;legal&#39;">legal</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '13, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/579b240041b084d221aaf999e0de2929?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fractal&#39;s gravatar image" />
<p><span>Fractal</span><br />
<span class="score" title="76 reputation points">76</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fractal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24501" class="comments-container">
<span id="24502"></span>
<div id="comment-24502" class="comment">
<div id="post-24502-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, the simplified boundaries can easily be extracted from the SVG map, so it’s a bit strange if the SVG can be in the public domain.</p>
</div>
<div id="comment-24502-info" class="comment-info">
<span class="comment-age">(23 Jul '13, 23:10)</span> <span class="comment-user userinfo">Fractal</span>
</div>
</div>
</div>
<div id="comment-tools-24501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24501-form-container" class="comment-form-container">
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

<span id="24512"></span>

<div id="answer-container-24512" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24512-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will not get binding legal advice from anyone unless you hire a lawyer, but I'll try and summarise past discussions from the <a href="http://lists.openstreetmap.org/listinfo/legal-talk">legal-talk mailing list</a> for you:</p>
<ol>
<li><p>Yes, the polygons can be reverse-engineered from the SVG, however you would thereby create a database again to which ODbL would apply even if the SVG wasn't under ODbL. The database rights persist even when the data is transported through a differently licensend channel. This is comparable to something like patents - where you can have a description of a process where the description is in the public domain, but if you want to execute it you might have to apply for a license from the patent holder.</p></li>
<li><p>You would probably be expected to share the raw, simplified polygons (which are a database derived from OSM) under the ODbL.</p></li>
<li><p>You can choose any license for your produced work but you have to attribute OSM. The exact wording is that: <em>You must include a notice associated with the Produced Work reasonably calculated to make any Person that uses, views, accesses, interacts with, or is otherwise exposed to the Produced Work aware that Content was obtained from the Database;</em> some interpretations conclude from this that not only do you have to attribute OSM, but you also have to make sure that if your work is again modified, used, or passed on, everyone down the line must be made aware of the data provenance, and hence the license chosen must at least have a persistent attribution clause, making PD unsuitable.</p></li>
</ol>
<p>This is just opinions from a bunch of interested people on the mailing list; not legal advice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '13, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24512" class="comments-container">
&#10;</div>
<div id="comment-tools-24512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24512-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24509"></span>

<div id="answer-container-24509" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24509-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>[I'm not a lawyer and have not read the <a href="http://opendatacommons.org/licenses/odbl/1.0/">legal document</a> for this scenario.]</p>
<p>Based on their FAQ, <a href="http://wiki.openstreetmap.org/wiki/Legal_FAQ#3c._If_I_make_something_with_OSM_data.2C_do_I_now_have_to_apply_your_license_to_my_whole_work.3F">Produced Work</a> does not require the same license.</p>
<p>However, you are required to provide attribution (credit) to OSM which is also <a href="http://wiki.openstreetmap.org/wiki/Legal_FAQ#3a._I_would_like_to_use_OpenStreetMap_maps._How_should_I_credit_you.3F">specified</a> in the form "© OpenStreetMap contributors." This is an odd requirement as it says to give credit to OSM a copyright to OSM must be attached. I suppose that does not specify a license; your produced work will not be under ODbL or Creative Commons (unless you put it there, and if we believe the FAQ).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '13, 07:53</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-24509" class="comments-container">
&#10;</div>
<div id="comment-tools-24509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24509-form-container" class="comment-form-container">
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

