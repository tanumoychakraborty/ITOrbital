package com.data.collection.sample.data_collection;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class TwitterDTO {

	private Long id;
	private String status;
	private Map<Long,String> comments = new HashMap<Long,String>();
	private int retweets = 0;
	private int liked = 0;
	
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public String getStatus() {
		return status;
	}
	public void setStatus(String status) {
		this.status = status;
	}
	public Collection<String> getComments() {
		return comments.values();
	}
	public void setComment(Long id, String comment) {
		this.comments.put(id, comment);
	}
	public int getRetweets() {
		return retweets;
	}
	public void setRetweets(int retweets) {
		this.retweets = retweets;
	}
	public int getLiked() {
		return liked;
	}
	public void setLiked(int liked) {
		this.liked = liked;
	}
	
}
