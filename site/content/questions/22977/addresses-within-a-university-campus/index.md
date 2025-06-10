+++
type = "question"
title = "Addresses within a University Campus"
description = '''I&#x27;m just adding some postcodes to one of the Nottingham University campus sites and realise that the available Open Data for addresses within the campus means that the addresses don&#x27;t fit neatly in existing OSM addressing schemas. I am sure this issue affects many large campus sites (Universities, H...'''
date = "2013-06-03T10:39:00Z"
lastmod = "2013-06-03T19:39:00Z"
weight = 22977
keywords = [ "building", "university", "addressing" ]
aliases = [ "/questions/22977" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Addresses within a University Campus](/questions/22977/addresses-within-a-university-campus)

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
<span id="post-22977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22977-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm just adding some postcodes to one of the Nottingham University campus sites and realise that the available Open Data for addresses within the campus means that the addresses don't fit neatly in existing OSM addressing schemas. I am sure this issue affects many large campus sites (Universities, Hospitals, Commercial sites).</p>
<p>Most, if not all buildings share the following address elements University of Nottingham, University Park, Nottingham NG7 2RD. The latter two are OK: one is <code>addr:city</code>, the <code>addr:postcode</code>, but the former is an organisation and the latter an area, which contains many named roads. I expect that there are other organisations sited on University Park (such as the <a href="http://www.ihr.mrc.ac.uk/pages/contactUs">Medical Research Council Institute of Hearing Research</a>).</p>
<p>It is conceivable that one could treat "University Park" as a street name, but I would regard that as highly misleading. Therefore I would like to know :</p>
<p><strong>Are there viable alternative approaches to mapping addresses on campus sites?</strong></p>
<p>Note: this is an example of how addresses dont fit most people's <a href="http://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/">preconceptions</a>.</p>
<p>(I am aware of course about addr:full, but this question is aimed at finding ways of avoiding this cop-out).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-university" rel="tag" title="see questions tagged &#39;university&#39;">university</span> <span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '13, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '13, 10:43</strong> </span></p>
</div>
</div>
<div id="comments-container-22977" class="comments-container">
<span id="22978"></span>
<div id="comment-22978" class="comment">
<div id="post-22978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you looked at other universities in the UK?</p>
<p>I found Heidelberg University in germany, which is a hotspot of OSM-related research, to use the actual street names on the OSM buildings, and to not have a all-encompassing campus relation.</p>
<p>University: <a href="http://www.openstreetmap.org/?lat=49.41581&amp;lon=8.67376&amp;zoom=16&amp;layers=M">http://www.openstreetmap.org/?lat=49.41581&amp;lon=8.67376&amp;zoom=16&amp;layers=M</a></p>
<p>One building: <a href="http://www.openstreetmap.org/browse/way/69693726">http://www.openstreetmap.org/browse/way/69693726</a></p>
</div>
<div id="comment-22978-info" class="comment-info">
<span class="comment-age">(03 Jun '13, 12:17)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="22983"></span>
<div id="comment-22983" class="comment">
<div id="post-22983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wonder whether this is just a case of <em><a href="http://wiki.openstreetmap.org/wiki/Tag:place%3Dneighbourhood">place=neighbourhood</a></em> (as an area) and <em>name=University Park</em>.</p>
</div>
<div id="comment-22983-info" class="comment-info">
<span class="comment-age">(03 Jun '13, 14:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22993"></span>
<div id="comment-22993" class="comment">
<div id="post-22993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@gormo</span>, older universities such as Heidelberg, Oxford, Cambridge, many parts of London tend to be in scattered buildings on named streets. Nottingham is an example of a fairly modern university which until 20 years ago was more or less entirely concentrated on one site "University Park".</p>
<p>Adding street names or even locality names as parts of the address would be totally incorrect. Many of the buildings, for instance the area known as Science City are not located on roads.</p>
<p><span>@scai</span> place=neighbourhood is just another fudge because there is no way to know how to interpret it for addressing</p>
</div>
<div id="comment-22993-info" class="comment-info">
<span class="comment-age">(03 Jun '13, 19:39)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22977-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

