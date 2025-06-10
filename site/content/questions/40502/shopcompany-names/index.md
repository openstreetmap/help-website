+++
type = "question"
title = "shop/company names"
description = '''Am I discouraged to use short_name, or maybe name:simple in the example below:  name=Syarikat Perkakasan Allplusplus Sdn Bhd (name:ms) name:en=Allplusplus Hardware Company Sdn Bhd (as seen on shop sign along with name:ms) name:simple=Allplusplus short_name=A++ (as seen on shop logo)  I know there ar...'''
date = "2015-01-21T07:09:00Z"
lastmod = "2015-01-22T17:15:00Z"
weight = 40502
keywords = [ "namesimple", "name", "short_name" ]
aliases = [ "/questions/40502" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [shop/company names](/questions/40502/shopcompany-names)

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
<span id="post-40502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40502-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Am I discouraged to use short_name, or maybe name:simple in the example below:</p>
<ul>
<li>name=Syarikat Perkakasan Allplusplus Sdn Bhd (name:ms)</li>
<li>name:en=Allplusplus Hardware Company Sdn Bhd (as seen on shop sign along with name:ms)</li>
<li>name:simple=Allplusplus</li>
<li>short_name=A++ (as seen on shop logo)</li>
</ul>
<p>I know there are longer names in other countries, so a shorter name seems logical to help renderers. short_name seems to be for initials abbreviations, so I thought why not use name:simple? Currently name:simple is probably only used for country names, but why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-namesimple" rel="tag" title="see questions tagged &#39;namesimple&#39;">namesimple</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-short_name" rel="tag" title="see questions tagged &#39;short_name&#39;">short_name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '15, 07:09</strong></p>
<img src="https://secure.gravatar.com/avatar/edf8bc160bbf7f47d6cbc6979120b2c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raito&#39;s gravatar image" />
<p><span>raito</span><br />
<span class="score" title="302 reputation points">302</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raito has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '15, 07:11</strong> </span></p>
</div>
</div>
<div id="comments-container-40502" class="comments-container">
<span id="40513"></span>
<div id="comment-40513" class="comment">
<div id="post-40513-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I looked at 2 cases of name:simple, France and Singapore. I don't understand why they use it, as it is exactly the same as name. Furthermore, there is no wiki page on name:simple. IMHO it's doubtful that e.g. Nominatim wil recognize the tag. Maybe it's better to use loc_name, which is documented on the wiki ?</p>
</div>
<div id="comment-40513-info" class="comment-info">
<span class="comment-age">(21 Jan '15, 20:22)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="40515"></span>
<div id="comment-40515" class="comment">
<div id="post-40515-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, the way name:simple is used right now doesn't seem to add anything new. But I think it could be made useful for helping renderers easily decide what text to render if the name is too long. I thought loc_name is for something completely different from the name, but I guess it can do.</p>
<p>If I may add, how about using the official_name tag which was also meant to be used for countries? - name=Allplusplus - official_name=Syarikat Perkakasan Allplusplus Sdn Bhd - official_name:en=Allplusplus Hardware Company Sdn Bhd - short_name=A++</p>
</div>
<div id="comment-40515-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 04:31)</span> <span class="comment-user userinfo">raito</span>
</div>
</div>
<span id="40520"></span>
<div id="comment-40520" class="comment">
<div id="post-40520-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><em>short_name</em> is not just for initials, it can be used for any abbreviation. I don't see a need for another short/simple name key.</p>
</div>
<div id="comment-40520-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 09:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="40538"></span>
<div id="comment-40538" class="comment">
<div id="post-40538-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>alt_name is also an option.</p>
</div>
<div id="comment-40538-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 17:15)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-40502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40502-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

