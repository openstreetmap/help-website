+++
type = "question"
title = "umap installation: postgresql connection error"
description = '''I try to install umap on an alwaysdata server.  I follow this tutorial : https://umap-project.readthedocs.io/en/latest/install/ At the migrate step umap migrate  i have this error:  File &quot;/home/*******/umap/lib/python3.6/site-packages/django/db/backends/base/base.py&quot;, line 171, in connect   self.con...'''
date = "2017-04-04T10:37:00Z"
lastmod = "2017-04-22T10:21:00Z"
weight = 55468
keywords = [ "migrate", "installation", "umap", "postgresql", "local.py" ]
aliases = [ "/questions/55468" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [umap installation: postgresql connection error](/questions/55468/umap-installation-postgresql-connection-error)

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
<span id="post-55468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I try to install umap on an alwaysdata server.</p>
<p>I follow this tutorial : <a href="https://umap-project.readthedocs.io/en/latest/install/">https://umap-project.readthedocs.io/en/latest/install/</a></p>
<p>At the migrate step</p>
<pre><code>umap migrate</code></pre>
<p>i have this error:</p>
<pre><code>File &quot;/home/*******/umap/lib/python3.6/site-packages/django/db/backends/base/base.py&quot;, line 171, in connect                                                                                   
    self.connection = self.get_new_connection(conn_params)                                                                                                                                    
File &quot;/home/*******/umap/lib/python3.6/site-packages/django/db/backends/postgresql/base.py&quot;, line 176, in get_new_connection                                                                  
    connection = Database.connect(**conn_params)                                                                                                                                              
File &quot;/home/*******/umap/lib/python3.6/site-packages/psycopg2/__init__.py&quot;, line 164, in connect                                                                                              
    conn = _connect(dsn, connection_factory=connection_factory, async=async)                                                                                                                  
django.db.utils.OperationalError: could not connect to server: No such file or directory                                                                                                      
        Is the server running locally and accepting                                                                                                                                           
        connections on Unix domain socket &quot;/var/run/postgresql/.s.PGSQL.5432&quot;?</code></pre>
<p>This is my local.py (i have try lot of things for the host:</p>
<pre><code>SECRET_KEY = &#39;********&#39;                                                                                                                                                                    
INTERNAL_IPS = (&#39;127.0.0.1&#39;, )                                                                                                                                                                
ALLOWED_HOSTS = [&#39;*&#39;, &#39;postgresql-&lt;accountname&gt;.alwaysdata.net&#39;,]
&#10;DEBUG = True
&#10;ADMINS = (                                                                                                                                                                                    
    (&#39;You&#39;, &#39;your@email&#39;),                                                                                                                                                                    
)                                                                                                                                                                                             
MANAGERS = ADMINS
&#10;DATABASES = {                                                                                                                                                                                 
    &#39;default&#39;: {                                                                                                                                                                              
        &#39;ENGINE&#39;: &#39;django.contrib.gis.db.backends.postgis&#39;,                                                                                                                                   
        &#39;NAME&#39;: &#39;********_umap&#39;,                                                                                                                                                                 
        &#39;USER&#39;: &#39;********&#39;,                                                                                                                                                                      
        &#39;PASSWORD&#39;: &#39;********&#39;                                                                                                                                                             
        &#39;HOST&#39;: &#39;postgresql-&lt;accountname&gt;.alwaysdata.net&#39;,                                                                                                                                                  
        &#39;PORT&#39;: &#39;5432&#39;,                                                                                                                                                                       
        &#39;DATABASE_HOST&#39; = &#39;postgresql-&lt;accountname&gt;.alwaysdata.net&#39;,                                                                                                                                        
    }                                                                                                                                                                                         
}</code></pre>
<p>The alwaysdata team haven't find a solution for my problem. <a href="https://forum.alwaysdata.com/viewtopic.php?id=4763">https://forum.alwaysdata.com/viewtopic.php?id=4763</a></p>
<p>Have you any idea?</p>
<p>Thanks a lot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-migrate" rel="tag" title="see questions tagged &#39;migrate&#39;">migrate</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-local.py" rel="tag" title="see questions tagged &#39;local.py&#39;">local.py</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '17, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/374bf7c432b5fdaf4aaaef3ebdbf90b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Suryavarman&#39;s gravatar image" />
<p><span>Suryavarman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Suryavarman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Apr '17, 23:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55468" class="comments-container">
&#10;</div>
<div id="comment-tools-55468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55468-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="55483"></span>

<div id="answer-container-55483" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55483-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The last three lines of the error message are pretty clear, aren' they? It's expecting to connect to Postgres via a named pipe at /var/run/postgresql/.s.PGSQL.5432, but that file doesn't exist. Does anything named similarly exist in /var/run/postgresql/? Can you see the server running when you type "ps aux | grep postgres"? It looks like umap (which I don't have a clue about, sorry) is actually supposed to use an IP socket to connect but somehow the database adapter is forced to only try the Unix socket. Maybe psycopg2 has some kind of config file?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Apr '17, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d62eaa0c9cab6317d2887bfe6bd2163b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbethke&#39;s gravatar image" />
<p><span>mbethke</span><br />
<span class="score" title="381 reputation points">381</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbethke has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-55483" class="comments-container">
&#10;</div>
<div id="comment-tools-55483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55483-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55734"></span>

<div id="answer-container-55734" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55734-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks a lot for your answer. I'm sorry for the delay.</p>
<p>The folder /var/run/postgresql/ doesn't exist. "ps aux | grep postgres" return nothing</p>
<p>I haven't find any psycopg2 config file. From psycopg2/__init_.py def connect(dsn=None,<br />
database=None, user=None, password=None, host=None, port=None,<br />
connection_factory=None, cursor_factory=None, async=False, **kwargs):</p>
<p>the inputs values are:</p>
<p>user : None password : None database : **** # not the good one host : None</p>
<p>I have force the values inside this <strong>init</strong>.py file:</p>
<p>The output error is : django.db.utils.OperationalError: could not translate host name "postgresql−****.alwaysdata.net" to address: Name or service not known</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '17, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/374bf7c432b5fdaf4aaaef3ebdbf90b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Suryavarman&#39;s gravatar image" />
<p><span>Suryavarman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Suryavarman has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '17, 15:17</strong> </span></p>
</div>
</div>
<div id="comments-container-55734" class="comments-container">
<span id="55740"></span>
<div id="comment-55740" class="comment">
<div id="post-55740-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>meta: please login and then use the "add new comment" button below mbethke's answer if you are commenting on it. Afterwards please delete this "answer".</p>
</div>
<div id="comment-55740-info" class="comment-info">
<span class="comment-age">(22 Apr '17, 02:38)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55734" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55734-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55745"></span>

<div id="answer-container-55745" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55745-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>always data have solve my last bug: postgresql−<strong><em>*.alwaysdata.net has to be ( "−" -&gt; "-" ) postgresql-</em></strong>*.alwaysdata.net</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '17, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/374bf7c432b5fdaf4aaaef3ebdbf90b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Suryavarman&#39;s gravatar image" />
<p><span>Suryavarman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Suryavarman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55745" class="comments-container">
&#10;</div>
<div id="comment-tools-55745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55745-form-container" class="comment-form-container">
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

