+++
type = "question"
title = "I get  a lot of deprication messages when running rake"
description = '''One thing i did different from the rail port tutorial is changing the version of an installed library. I had this: gem install -v=2.3.14 rails changed into this: gem install -v=3.1 rails I also get a lot of these errors when running rake test. NOTE: Gem::SourceIndex#initialize is deprecated with no ...'''
date = "2011-10-24T09:35:00Z"
lastmod = "2011-10-24T13:35:00Z"
weight = 8611
keywords = [ "rake", "osm", "rails" ]
aliases = [ "/questions/8611" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I get a lot of deprication messages when running rake](/questions/8611/i-get-a-lot-of-deprication-messages-when-running-rake)

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
<span id="post-8611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8611-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-8611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>One thing i did different from the rail port tutorial is changing the version of an installed library. I had this: <code>gem install -v=2.3.14 rails</code></p>
<p>changed into this: <code>gem install -v=3.1 rails</code></p>
<p>I also get a lot of these errors when running rake test.</p>
<pre><code>NOTE: Gem::SourceIndex#initialize is deprecated with no replacement. It will be removed on or after 2011-11-01.
Gem::SourceIndex#initialize called from /usr/lib/ruby/gems/1.8/gems/rails-2.3.14/lib/rails/vendor_gem_source_index.rb:100.
NOTE: Gem::SourceIndex#add_spec is deprecated, use Specification.add_spec. It will be removed on or after 2011-11-01.
Gem::SourceIndex#add_spec called from /usr/local/lib/site_ruby/1.8/rubygems/source_index.rb:91.
NOTE: Gem::SourceIndex#add_spec is deprecated, use Specification.add_spec. It will be removed on or after 2011-11-01.
Gem::SourceIndex#add_spec called from /usr/local/lib/site_ruby/1.8/rubygems/source_index.rb:91.
NOTE: Gem.source_index is deprecated, use Specification. It will be removed on or after 2011-11-01.
Gem.source_index called from /usr/lib/ruby/gems/1.8/gems/rails-2.3.14/lib/rails/gem_dependency.rb:78.</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rake" rel="tag" title="see questions tagged &#39;rake&#39;">rake</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '11, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '11, 09:40</strong> </span></p>
</div>
</div>
<div id="comments-container-8611" class="comments-container">
&#10;</div>
<div id="comment-tools-8611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8611-form-container" class="comment-form-container">
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

<span id="8615"></span>

<div id="answer-container-8615" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8615-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not clear what you are trying to achieve. Rails 2.3 and Rails 3.1 are incompatible. The current code doesn't work on rails 3, and that's why the tutorial specifies the exact version of rails that's required. You should use that version.</p>
<p>There is work in progress to rewrite parts of the code in order to work with rails 3.1, but this is not yet complete. If you are interested in helping with the development, then see <a href="https://github.com/tomhughes/openstreetmap-website/tree/rails3">https://github.com/tomhughes/openstreetmap-website/tree/rails3</a> for the work so far.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '11, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-8615" class="comments-container">
<span id="8616"></span>
<div id="comment-8616" class="comment">
<div id="post-8616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but i installed that same version but still get the messages.</p>
</div>
<div id="comment-8616-info" class="comment-info">
<span class="comment-age">(24 Oct '11, 13:35)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8615-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8612"></span>

<div id="answer-container-8612" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8612-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is just deprication warnings. You can change the code to not use the deprecated functions and send the patch in a bug report so that it can work on newer versions. Note that you might want to keep the code backwards compatible by not using new functions and/or branching on version.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '11, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8612" class="comments-container">
<span id="8613"></span>
<div id="comment-8613" class="comment">
<div id="post-8613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>HOw to change the code? ANd into what should i change?</p>
</div>
<div id="comment-8613-info" class="comment-info">
<span class="comment-age">(24 Oct '11, 10:18)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8614"></span>
<div id="comment-8614" class="comment">
<div id="post-8614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i get this message too. Is it normal?</p>
<pre><code>$ rake gems:install
rake/rdoctask is deprecated.  Use rdoc/task instead (in RDoc 2.4.2+)</code></pre>
</div>
<div id="comment-8614-info" class="comment-info">
<span class="comment-age">(24 Oct '11, 12:10)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8612-form-container" class="comment-form-container">
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

