+++
type = "question"
title = "how to decode an user custom exception from GIOP stream?"
description = '''Hey all,  I have caught a GIOP stream by wireshark, which should contain my user custom exception propagation data between : my server(jboss iiop/jacorb) and my client(simple test to get threw exception from deploy jar on server) In my threw exception, I defined a variable &quot;i&quot;, and want to check tha...'''
date = "2012-09-28T19:15:00Z"
lastmod = "2012-09-28T19:15:00Z"
weight = 14610
keywords = [ "decode", "exception", "giop" ]
aliases = [ "/questions/14610" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to decode an user custom exception from GIOP stream?](/questions/14610/how-to-decode-an-user-custom-exception-from-giop-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14610-score" class="post-score" title="current number of votes">0</div><span id="post-14610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey all,</p><p>I have caught a GIOP stream by wireshark, which should contain my user custom exception propagation data between :</p><p>my server(jboss iiop/jacorb) and my client(simple test to get threw exception from deploy jar on server)</p><p>In my threw exception, I defined a variable "i", and want to check that variable value in my GIOP stream(because when I read back that value from client side, it's wrong).</p><p>But from the view of my sub-data, I can only see part of my exception stream data, like my exception "class name" and "error message" when I created it, by my variable value is still encoded, so I assume that the default dissector can only decode the data of an JAVA Exception type, but not other data of a custom exception.</p><p>Does anyone have the same experience and know what should I do with wireshark to make my defined variable i visible and readable?</p><p>this is my exception looks like in java:</p><pre><code>public class NegativeArgumentException extends Exception
{
   int i;

   public NegativeArgumentException(int i) 
   {
      super(&quot;Negative argument: &quot; + i);
      this.i = i;
   }

   public int getNegativeArgument() 
   {
      return i;
   }
}</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-exception" rel="tag" title="see questions tagged &#39;exception&#39;">exception</span> <span class="post-tag tag-link-giop" rel="tag" title="see questions tagged &#39;giop&#39;">giop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '12, 19:15</strong></p><img src="https://secure.gravatar.com/avatar/4ee2c7bed85c902a4f8a7af63b692792?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="soul2zimate&#39;s gravatar image" /><p><span>soul2zimate</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="soul2zimate has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Sep '12, 23:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-14610" class="comments-container"></div><div id="comment-tools-14610" class="comment-tools"></div><div class="clear"></div><div id="comment-14610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

