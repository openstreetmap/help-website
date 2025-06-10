+++
type = "question"
title = "a missing uk postal code"
description = '''Hi, and thanks for your previous help. I upgraded to Nominatim 2.2, and added the UK postal code data. I can see the postal code &quot;NE33 5PZ&quot; in the file gb_postcode_data.sql. When I query &quot;search?postalcode=NE33+5PZ&amp;amp;country=uk&quot; my server returns an optional address in postal code NE33 4JP, while ...'''
date = "2014-03-24T14:41:00Z"
lastmod = "2014-03-24T16:25:00Z"
weight = 31847
keywords = [ "postalcode", "nominatim", "gb", "uk" ]
aliases = [ "/questions/31847" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [a missing uk postal code](/questions/31847/a-missing-uk-postal-code)

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
<span id="post-31847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31847-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, and thanks for your previous help.</p>
<p>I upgraded to Nominatim 2.2, and added the UK postal code data.</p>
<p>I can see the postal code "NE33 5PZ" in the file gb_postcode_data.sql.</p>
<p>When I query "search?postalcode=NE33+5PZ&amp;country=uk"</p>
<p>my server returns an optional address in postal code NE33 4JP, while the public server returns no result.</p>
<p>When I query "street=dean+road&amp;postalcode=NE33+5PZ&amp;country=uk"</p>
<p>both my server and the public server return 3 optional addresses, only my server includes a postal code for each option, but none of them are the one I'm looking for.</p>
<p>so: 1) hasn't the public server been updated to 2.2 yet? 2) why can't I find the postal code "NE33 5PZ" even though I see it in gb_postcode_data.sql:</p>
<p>956675 NE33 5PZ 0101000020E61000007D491A914EEFF6BF710A1A57257E4B40</p>
<p>Thanks a lot, Raz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postalcode" rel="tag" title="see questions tagged &#39;postalcode&#39;">postalcode</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-gb" rel="tag" title="see questions tagged &#39;gb&#39;">gb</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '14, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/84ebb95a07dd884e34f0170b07b1d652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RazAlon&#39;s gravatar image" />
<p><span>RazAlon</span><br />
<span class="score" title="61 reputation points">61</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RazAlon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '14, 08:14</strong> </span></p>
</div>
</div>
<div id="comments-container-31847" class="comments-container">
<span id="31854"></span>
<div id="comment-31854" class="comment">
<div id="post-31854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I get the expected results from Nominatim for this postcode: a Free the Postcode entry and several mapped places adjacent to Dean Road, including one the Stanhope Parade Health Centre which has a postcode but not the one you are after. As no OSM objects are associated with this postcode that's what I would expect.</p>
</div>
<div id="comment-31854-info" class="comment-info">
<span class="comment-age">(24 Mar '14, 16:25)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31847-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

