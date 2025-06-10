+++
type = "question"
title = "Bing Bird&#x27;s Eye imagery; policy changed, misread?"
description = '''Bing offers some aerial imagery for use by osm editors, in osm editor apps, via an API. “Bird&#x27;s Eye” is Microsoft&#x27;s name for a separate category of their imagery. It contains amazing, high-resolution photos from low-flying aircraft, but it is only available in select areas, is often at rather obliqu...'''
date = "2021-06-15T14:37:00Z"
lastmod = "2021-09-19T14:53:00Z"
weight = 80584
keywords = [ "aerial_imagery", "bing", "license" ]
aliases = [ "/questions/80584" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bing Bird's Eye imagery; policy changed, misread?](/questions/80584/bing-birds-eye-imagery-policy-changed-misread)

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
<span id="post-80584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80584-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Bing offers some aerial imagery for use by osm editors, in osm editor apps, via an API. “Bird's Eye” is Microsoft's name for a separate category of their imagery. It contains amazing, high-resolution photos from low-flying aircraft, but it is only available in select areas, is often at rather oblique angles, and is poorly aligned. Back to osm, I found an <a href="https://help.openstreetmap.org/questions/62181/bing-birds-eye-images">earlier question</a> here, on the use of Bird's Eye imagery, with only one answer, which said it is not permitted.</p>
<p>That answer cited the Bing Maps wiki article, which did make explicit that it was not allowed by Microsoft's license. But some time later, an <a href="https://wiki.openstreetmap.org/w/index.php?title=Bing_Maps&amp;diff=1639586&amp;oldid=1639554">edit to the article</a> removed the mention of the Bird's Eye restriction, with commit comment "precision". It's remained unmentioned there since then.</p>
<h2 id="is-the-birds-eye-imagery-use-disallowed">Is the <em>Bird's Eye</em> imagery use disallowed?</h2>
<p>In an effort to determine the state of things for myself, I read the related ToU, "<a href="https://www.microsoft.com/en-us/maps/product/imagery-service-editor-app-apis-terms">Microsoft® Bing™ Maps Imagery Service Editor Application APIs Terms of Use</a>"</p>
<p>By my layperson reading of it, the following text seems to be all the relevant bits (unaltered, but heavily-trimmed, and emphasis mine):</p>
<p>      2. What rights do I have?<br />
            …<br />
            Further, we grant you the limited right to use <strong>Street Side</strong> imagery provided by the StreetSide API in read-only format solely as an additional source of corroborating ground truth within OpenStreetMap editing environments. You may not use the StreetSide API to extract StreetSide imagery or for any other use.</p>
<p>            Restrictions on your use: We do have some restrictions on your use of the service. <strong>You may not</strong>:<br />
                - use <strong>Bird's Eye, StreetSide, or Photosynth</strong> imagery (<strong>except as expressly set forth herein</strong>).</p>
<p>—and that's it. So Bird's Eye, StreetSide, and Photosynth imagery are explicitly restricted, except where they make exceptions. And there's only one exception: StreetSide for corroboration of ground truth while in an osm editor apps.</p>
<p>I'd hate for us to be violating Microsoft's generous license. Before I correct the wiki or go around the forum commenting on mentions of using Bird's Eye, I wanted to get the the bottom of it. Can you settle the matter?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aerial_imagery" rel="tag" title="see questions tagged &#39;aerial_imagery&#39;">aerial_imagery</span> <span class="post-tag tag-link-bing" rel="tag" title="see questions tagged &#39;bing&#39;">bing</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '21, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/55b16bb2545593ba830f2d1efd5516ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joel%20D%20Reid&#39;s gravatar image" />
<p><span>Joel D Reid</span><br />
<span class="score" title="166 reputation points">166</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joel D Reid has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-80584" class="comments-container">
<span id="80588"></span>
<div id="comment-80588" class="comment">
<div id="post-80588-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Basically you are allowed to use Bing imagery which appears in editors and not that which appears on the Bing site. Removing reference to Bird's Eye seems appropriate in a paragraph discussing the pitfalls of assuming standard orthoimagery is correctly rectified.</p>
</div>
<div id="comment-80588-info" class="comment-info">
<span class="comment-age">(15 Jun '21, 16:51)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="80589"></span>
<div id="comment-80589" class="comment">
<div id="post-80589-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> Agreed. I think the problem is any who read the wiki and head off to start mapping with the naïve takeaway, "Bing imagery is a licensed source!"</p>
</div>
<div id="comment-80589-info" class="comment-info">
<span class="comment-age">(15 Jun '21, 16:57)</span> <span class="comment-user userinfo">Joel D Reid</span>
</div>
</div>
<span id="81808"></span>
<div id="comment-81808" class="comment">
<div id="post-81808-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree with Joel D Reid. See my post on the wiki page discussion page: <a href="https://wiki.openstreetmap.org/wiki/Talk:Bing_Maps#Proposal_to_rework_the_header_paragraph_for_Bing_Aerial_Imagery_section">https://wiki.openstreetmap.org/wiki/Talk:Bing_Maps#Proposal_to_rework_the_header_paragraph_for_Bing_Aerial_Imagery_section</a></p>
</div>
<div id="comment-81808-info" class="comment-info">
<span class="comment-age">(19 Sep '21, 14:53)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
</div>
<div id="comment-tools-80584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80584-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

