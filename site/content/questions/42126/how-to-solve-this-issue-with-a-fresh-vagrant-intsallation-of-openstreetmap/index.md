+++
type = "question"
title = "How to solve this issue with a fresh vagrant intsallation of openstreetmap"
description = '''I made all the steps of a vagrant install And I connect to localhost:3000, I obtain an error 500 How I can solve it?  Here is the log in the ssh console:  [2015-04-05 10:37:58] INFO ruby 1.9.3 (2011-10-30) [x86_64-linux] [2015-04-05 10:37:58] INFO WEBrick::HTTPServer#start: pid=27112 port=3000  Star...'''
date = "2015-04-05T11:57:00Z"
lastmod = "2018-11-11T01:31:00Z"
weight = 42126
keywords = [ "vagrant", "installation" ]
aliases = [ "/questions/42126" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to solve this issue with a fresh vagrant intsallation of openstreetmap](/questions/42126/how-to-solve-this-issue-with-a-fresh-vagrant-intsallation-of-openstreetmap)

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
<span id="post-42126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42126-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I made all the steps of a vagrant install And I connect to localhost:3000, I obtain an error 500 How I can solve it?</p>
<p>Here is the log in the ssh console:</p>
<pre><code>[2015-04-05 10:37:58] INFO  ruby 1.9.3 (2011-10-30) [x86_64-linux]
[2015-04-05 10:37:58] INFO  WEBrick::HTTPServer#start: pid=27112 port=3000
&#10;Started GET &quot;/&quot; for 10.0.2.2 at 2015-04-05 10:39:28 +0000
  ActiveRecord::SchemaMigration Load (3.4ms)  SELECT &quot;schema_migrations&quot;.* FROM &quot;schema_migrations&quot;
Processing by SiteController#index as HTML
  Rendered site/index.html.erb within layouts/map (33.2ms)
  Rendered layouts/_search.html.erb (530.9ms)
  Rendered layouts/_search.html.erb (31.8ms)
  Rendered layouts/_flash.html.erb (3.8ms)
  Rendered layouts/_head.html.erb (16128.2ms)
  Rendered layouts/site.html.erb (16237.5ms)
Completed 500 Internal Server Error in 33688ms (ActiveRecord: 0.0ms)
&#10;ActionView::Template::Error (Invalid CSS after &quot;../common.scss&quot;: expected &quot;{&quot;, was &quot;&quot;
  (in /srv/openstreetmap-website/app/assets/stylesheets/ltr/common.scss:2)):
    3:   
    4:   
    5:   &lt;%= javascript_include_tag &quot;application&quot; %&gt;
    6:   &lt;%= stylesheet_link_tag &quot;small-#{dir}&quot;, :media =&gt; &quot;only screen and (max-width:721px)&quot; %&gt;
    7:   &lt;%= stylesheet_link_tag &quot;large-#{dir}&quot;, :media =&gt; &quot;screen and (min-width: 722px)&quot; %&gt;
    8:   &lt;%= stylesheet_link_tag &quot;print-#{dir}&quot;, :media =&gt; &quot;print&quot; %&gt;
    9:   &lt;%= stylesheet_link_tag &quot;leaflet-all&quot;, :media =&gt; &quot;screen, print&quot; %&gt;
  app/assets/stylesheets/ltr/common.scss:2
  app/views/layouts/_head.html.erb:6:in `_app_views_layouts__head_html_erb__2680021569999862732_65660600&#39;
  app/views/layouts/site.html.erb:3:in `_app_views_layouts_site_html_erb__4155754249160337287_65461020&#39;
  app/views/layouts/map.html.erb:83:in `_app_views_layouts_map_html_erb__1229493903015393840_58573620&#39;
  config/initializers/cors.rb:9:in `call&#39;
&#10;
  Rendered /var/lib/gems/1.9.1/gems/actionpack-4.2.1/lib/action_dispatch/middleware/templates/rescues/_source.erb (120.4ms)
  Rendered /var/lib/gems/1.9.1/gems/actionpack-4.2.1/lib/action_dispatch/middleware/templates/rescues/_trace.html.erb (31.3ms)
  Rendered /var/lib/gems/1.9.1/gems/actionpack-4.2.1/lib/action_dispatch/middleware/templates/rescues/_request_and_response.html.erb (5.5ms)
  Rendered /var/lib/gems/1.9.1/gems/actionpack-4.2.1/lib/action_dispatch/middleware/templates/rescues/template_error.html.erb within rescues/layout (258.2ms)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-vagrant" rel="tag" title="see questions tagged &#39;vagrant&#39;">vagrant</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '15, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/3835a78f4926d6d046bdc9a214d0e114?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Titi9876&#39;s gravatar image" />
<p><span>Titi9876</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Titi9876 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Apr '15, 12:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-42126" class="comments-container">
<span id="42135"></span>
<div id="comment-42135" class="comment">
<div id="post-42135-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Which steps did you do? Which manual/instructions did you use?</p>
</div>
<div id="comment-42135-info" class="comment-info">
<span class="comment-age">(06 Apr '15, 03:16)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
<span id="42137"></span>
<div id="comment-42137" class="comment">
<div id="post-42137-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I used the vagrant.md instructions.</p>
<p><a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/VAGRANT.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/VAGRANT.md</a></p>
<p>I downloaded vagrant for windows I installed it I installed github for windows, because I needed ssh, and git I have done the tutorial of vagrant Then I destroyed the vagrant used for the tutorial</p>
<p>Then I did what is described in the vagrant.md git clone git@github.com:openstreetmap/openstreetmap-website.git cd openstreetmap-website vagrant up vagrant ssh</p>
<p>then on the server : cd /srv/openstreetmap-website/ rails server --binding=0.0.0.0</p>
<p>then back to the PC : in Chrome : <a href="http://localhost:3000/">http://localhost:3000/</a></p>
<p>And I got the result that you can see above.</p>
</div>
<div id="comment-42137-info" class="comment-info">
<span class="comment-age">(06 Apr '15, 08:09)</span> <span class="comment-user userinfo">Titi9876</span>
</div>
</div>
<span id="58919"></span>
<div id="comment-58919" class="comment">
<div id="post-58919-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, i have the same problem , that author have. Can anyone help with this ? I've installed fresh Rails Port, via clonnig repo many times, but always there were problem at test:db step. Probably the problem in sass.</p>
</div>
<div id="comment-58919-info" class="comment-info">
<span class="comment-age">(02 Sep '17, 00:45)</span> <span class="comment-user userinfo">Нурик Нурметов</span>
</div>
</div>
<span id="58922"></span>
<div id="comment-58922" class="comment">
<div id="post-58922-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Pls do not ask questions in answers.</p>
</div>
<div id="comment-58922-info" class="comment-info">
<span class="comment-age">(02 Sep '17, 08:55)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="59446"></span>
<div id="comment-59446" class="comment">
<div id="post-59446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suppose that you've missed some steps, because probably style sheets were not pre-processed.</p>
</div>
<div id="comment-59446-info" class="comment-info">
<span class="comment-age">(06 Sep '17, 19:23)</span> <span class="comment-user userinfo">Sergey Karavay</span>
</div>
</div>
<span id="66731"></span>
<div id="comment-66731" class="comment not_top_scorer">
<div id="post-66731-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a similar problem with ltr/common.scss. I've figured out that it's caused by symlinks in VirtualBox shared folders. You can avoid it by not using VirtualBox shared folders. If I figure out how to make everything work without shared folders, I'll post an answer.</p>
</div>
<div id="comment-66731-info" class="comment-info">
<span class="comment-age">(09 Nov '18, 02:28)</span> <span class="comment-user userinfo">Krubo</span>
</div>
</div>
</div>
<div id="comment-tools-42126" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-42126-form-container" class="comment-form-container">
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

<span id="66744"></span>

<div id="answer-container-66744" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66744-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had a similar problem, although my error message was different. I'm using Vagrant on Windows 10, running git from Cygwin. My precise error message was: <code>Error: Invalid UTF-8 sequence on line 1 of app/assets/stylesheets/ltr/common.scss</code>. However, I think the problem is similar because it mentions the same file as your error:</p>
<pre><code>/srv/openstreetmap-website/app/assets/stylesheets/ltr/common.scss</code></pre>
<p>It turns out this file is a symlink, and it looks like VirtualBox is <a href="https://www.virtualbox.org/ticket/10085">less than fully graceful</a> in handling symlinks within folders that are shared between the guest and host. I haven't found a way to fix the issue directly, but I was able to work around it by cloning OSM into a non-shared folder on the guest machine, as follows:</p>
<pre><code>$ vagrant ssh
vagrant@ubuntu-bionic:~$ cd /srv
vagrant@ubuntu-bionic:/srv$ sudo mkdir osmw2
vagrant@ubuntu-bionic:/srv$ sudo chown vagrant:vagrant osmw2
vagrant@ubuntu-bionic:/srv$ cd osmw2
vagrant@ubuntu-bionic:/srv/osmw2$ git clone --depth=1 https://github.com/openstreetmap/openstreetmap-website.git
vagrant@ubuntu-bionic:/srv/osmw2$ cd openstreetmap-website
vagrant@ubuntu-bionic:/srv/osmw2/openstreetmap-website$ cp /srv/openstreetmap-website/config/application.yml config/
vagrant@ubuntu-bionic:/srv/osmw2/openstreetmap-website$ cp /srv/openstreetmap-website/config/database.yml config/
vagrant@ubuntu-bionic:/srv/osmw2/openstreetmap-website$ rails server --binding=0.0.0.0</code></pre>
<p>Then open your web browser and go to localhost:3000. (Note, this workaround doesn't let you share the code with your host machine, so if you want to edit code you have to do it on the guest VM, using command-line tools like vi and git.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '18, 01:31</strong></p>
<img src="https://secure.gravatar.com/avatar/6ad28c56201340399ec9c944dca247c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Krubo&#39;s gravatar image" />
<p><span>Krubo</span><br />
<span class="score" title="116 reputation points">116</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Krubo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '18, 02:43</strong> </span></p>
</div>
</div>
<div id="comments-container-66744" class="comments-container">
&#10;</div>
<div id="comment-tools-66744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66744-form-container" class="comment-form-container">
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

