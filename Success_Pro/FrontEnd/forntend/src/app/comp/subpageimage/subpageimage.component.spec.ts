import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SubpageimageComponent } from './subpageimage.component';

describe('SubpageimageComponent', () => {
  let component: SubpageimageComponent;
  let fixture: ComponentFixture<SubpageimageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SubpageimageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SubpageimageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
