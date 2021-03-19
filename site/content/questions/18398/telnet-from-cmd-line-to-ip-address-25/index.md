+++
type = "question"
title = "Telnet from cmd line to ip address 25"
description = '''New to wireshark :} When I do a telnet fqdn 25 - I see the traffic on port 587 and not 25. I thought that I should be able to see the traffic destinated for port 25 being &quot;redirected&quot; to 587. But I do not. The first packet from my machine is to port 587 ? I am not understanding this.'''
date = "2013-02-07T06:09:00Z"
lastmod = "2013-02-07T16:34:00Z"
weight = 18398
keywords = [ "25", "587", "tcp", "show" ]
aliases = [ "/questions/18398" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Telnet from cmd line to ip address 25](/questions/18398/telnet-from-cmd-line-to-ip-address-25)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18398-score" class="post-score" title="current number of votes">0</div><span id="post-18398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>New to wireshark :} When I do a telnet fqdn 25 - I see the traffic on port 587 and not 25. I thought that I should be able to see the traffic destinated for port 25 being "redirected" to 587. But I do not. The first packet from my machine is to port 587 ? I am not understanding this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-25" rel="tag" title="see questions tagged &#39;25&#39;">25</span> <span class="post-tag tag-link-587" rel="tag" title="see questions tagged &#39;587&#39;">587</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-show" rel="tag" title="see questions tagged &#39;show&#39;">show</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '13, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/30677655b491fb080dda6dd57c9a9117?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdcowboy&#39;s gravatar image" /><p><span>mdcowboy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdcowboy has no accepted answers">0%</span></p></div></div><div id="comments-container-18398" class="comments-container"><span id="18399"></span><div id="comment-18399" class="comment"><div id="post-18399-score" class="comment-score"></div><div class="comment-text"><p>Why do you expect a redirect to port 587 at all? A "telnet nameofhost 25" should always lead to a SYN being sent to port 25, at least if you're talking about the standard windows telnet program...</p><p>Do you have some sort of redirection software running, or why do you think that oyu should be able to see traffic for port 25 being "redirected"?</p></div><div id="comment-18399-info" class="comment-info"><span class="comment-age">(07 Feb '13, 06:15)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="18400"></span><div id="comment-18400" class="comment"><div id="post-18400-score" class="comment-score"></div><div class="comment-text"><p>TX- I expect to see dst port of 25. I am using the standard windows telnet program. I know that port 587 is also open to the dest addr.</p></div><div id="comment-18400-info" class="comment-info"><span class="comment-age">(07 Feb '13, 06:18)</span> <span class="comment-user userinfo">mdcowboy</span></div></div><span id="18429"></span><div id="comment-18429" class="comment"><div id="post-18429-score" class="comment-score"></div><div class="comment-text"><blockquote><p>When I do a telnet fqdn 25<br />
The first packet from my machine is to port 587 ? I am not understanding this.</p></blockquote><p>That sounds strange.</p><ul><li>Did you capture on the same machine where you ran telnet?</li><li>Can you post a capture file somewhere (google docs, cloudshark.org, etc.)?</li></ul></div><div id="comment-18429-info" class="comment-info"><span class="comment-age">(07 Feb '13, 16:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-18398" class="comment-tools"></div><div class="clear"></div><div id="comment-18398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18401"></span>

<div id="answer-container-18401" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18401-score" class="post-score" title="current number of votes">0</div><span id="post-18401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just did what you did: running <code>telnet ip-address 25</code> and captured it with Wireshark on the same PC (which results to broken checksums, don't worry, that's normal). Result can be seen here:</p><p><a href="http://www.cloudshark.org/captures/21904d613ef7">http://www.cloudshark.org/captures/21904d613ef7</a></p><p>This is how it should look like for you, too. If it doesn't, something is going wrong.</p><p>P.S: smtp command &amp; control by console. Oldschool! :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '13, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-18401" class="comments-container"></div><div id="comment-tools-18401" class="comment-tools"></div><div class="clear"></div><div id="comment-18401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

